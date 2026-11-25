(() => {
  const canvas = document.querySelector('.footer-wave');
  const footer = canvas?.closest('footer');
  const button = document.querySelector('.footer-motion-toggle');
  if (!canvas || !button || !footer) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let width = 0, height = 0, frame = 0, lastTime = 0, visible = false;
  let events = [];
  const perspective = 0.55;
  const words = [];
  // Keep real, selectable text while giving each word a small wave response.
  footer.querySelectorAll(':scope > span, .footer-wave-hint').forEach(line => {
    const fragments = line.textContent.match(/\S+|\s+/g) || [];
    line.replaceChildren(...fragments.map(text => {
      if (!text.trim()) return document.createTextNode(text);
      const word = document.createElement('span');
      word.className = 'footer-wave-word';
      word.textContent = text;
      words.push({element: word, x: 0, y: 0});
      return word;
    }));
  });
  // Move the complete control gently, preserving its label and click handler.
  words.push({element: button, x: 0, y: 0});
  function displacement(x, y, fronts) {
    let dxTotal = 0, dyTotal = 0, strength = 0;
    for (const front of fronts) {
      const dx = x - front.x, dy = (y - front.y) / perspective;
      const distance = Math.hypot(dx, dy);
      const pulse = Math.exp(-(((distance - front.radius) / 22) ** 2)) * front.alpha;
      dxTotal += dx / (distance || 1) * pulse * 5;
      dyTotal += dy / (distance || 1) * pulse * 3;
      strength += pulse;
    }
    return {x: Math.max(-6, Math.min(6, dxTotal)), y: Math.max(-4, Math.min(4, dyTotal)), strength: Math.min(strength, 1)};
  }
  function draw() {
    ctx.clearRect(0, 0, width, height);
    const columns = Math.min(100, Math.max(32, Math.round(width / 14)));
    const fronts = events.flatMap(event => [0, 0.32, 0.64].map(delay => ({
      x: event.u * width, y: event.v * height,
      radius: (event.age - delay) * 180,
      // Decorative attenuation: waves spread out and lose strength with distance.
      alpha: Math.max(0, 1 - event.age / 5)
        / Math.sqrt(1 + Math.max(0, (event.age - delay) * 180) / 90)
        * Math.exp(-Math.max(0, (event.age - delay) * 180) / 1100)
    })).filter(front => front.radius > 0));
    const rows = Math.max(8, Math.round(height / 9));
    for (let row = 0; row < rows; row++) {
      for (let col = 0; col < columns; col++) {
        const u = col / (columns - 1);
        const x = 6 + u * (width - 12), y = 5 + row / (rows - 1) * (height - 10);
        const motion = displacement(x, y, fronts);
        const strength = motion.strength;
        const offsetX = motion.x, offsetY = motion.y;
        ctx.fillStyle = `rgba(255,255,255,${0.18 + strength * 0.60})`;
        ctx.beginPath();
        ctx.arc(x + offsetX, y + offsetY, 1.05 + strength * 0.65, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    for (const word of words) {
      const motion = reduced.matches ? {x: 0, y: 0} : displacement(word.x, word.y, fronts);
      word.element.style.transform = `translate(${motion.x.toFixed(2)}px, ${motion.y.toFixed(2)}px)`;
    }
    for (const front of fronts) {
      ctx.strokeStyle = `rgba(255,255,255,${front.alpha * 0.32})`;
      ctx.lineWidth = 0.8;
      ctx.beginPath();
      ctx.ellipse(front.x, front.y, front.radius, front.radius * perspective, 0, 0, Math.PI * 2);
      ctx.stroke();
    }
    for (const event of events) {
      const x = event.u * width, y = event.v * height;
      const alpha = Math.max(0, 1 - event.age / 5);
      const glow = ctx.createRadialGradient(x, y, 0, x, y, 17);
      glow.addColorStop(0, `rgba(255,45,70,${alpha * 0.85})`);
      glow.addColorStop(1, 'rgba(255,45,70,0)');
      ctx.fillStyle = glow;
      ctx.beginPath(); ctx.arc(x, y, 17, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = `rgba(255,48,79,${alpha})`;
      ctx.beginPath(); ctx.arc(x, y, 3.5, 0, Math.PI * 2); ctx.fill();
    }
  }
  function animate(time) {
    frame = 0;
    if (!visible || document.hidden || reduced.matches || !events.length) return;
    const delta = lastTime ? Math.min(time - lastTime, 50) / 1000 : 0;
    lastTime = time;
    events.forEach(event => { event.age += delta; });
    events = events.filter(event => event.age < 5);
    draw();
    if (events.length) frame = requestAnimationFrame(animate);
  }
  function sync() {
    cancelAnimationFrame(frame); frame = 0; lastTime = 0;
    draw();
    if (visible && !document.hidden && !reduced.matches && events.length) frame = requestAnimationFrame(animate);
  }
  function trigger(u = 0.5, v = 0.5) {
    events = events.slice(-5);
    events.push({u, v, age: reduced.matches ? 0.35 : 0});
    sync();
  }
  footer.addEventListener('click', event => {
    if (event.target.closest('button, a')) return;
    const bounds = canvas.getBoundingClientRect();
    trigger((event.clientX - bounds.left) / bounds.width, (event.clientY - bounds.top) / bounds.height);
  });
  canvas.addEventListener('keydown', event => {
    if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); trigger(); }
  });
  button.textContent = 'Generate earthquake';
  button.removeAttribute('aria-pressed');
  button.hidden = false;
  button.addEventListener('click', () => trigger(0.04 + Math.random() * 0.92, 0.08 + Math.random() * 0.84));
  reduced.addEventListener('change', () => { events = []; sync(); });
  document.addEventListener('visibilitychange', sync);
  new IntersectionObserver(entries => { visible = entries[0].isIntersecting; sync(); }).observe(canvas);
  function resize() {
    const bounds = canvas.getBoundingClientRect();
    width = bounds.width; height = bounds.height;
    const ratio = Math.min(devicePixelRatio || 1, 2);
    canvas.width = Math.round(width * ratio); canvas.height = Math.round(height * ratio);
    ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
    words.forEach(word => { word.element.style.transform = ''; });
    words.forEach(word => {
      const rect = word.element.getBoundingClientRect();
      word.x = rect.left + rect.width / 2 - bounds.left;
      word.y = rect.top + rect.height / 2 - bounds.top;
    });
    draw();
  }
  new ResizeObserver(resize).observe(footer);
  document.fonts?.ready.then(resize);
})();
