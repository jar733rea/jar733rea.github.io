# Juan Rea-Avila — academic website

Personal academic website hosted with GitHub Pages.

## Update the website

Edit `content/` for Bio, Publications, Activities, and Contact. Edit `build.py` for the homepage and shared navigation, and `style.css` for appearance. Images and the CV are in `assets/`.

Preview locally:

```sh
python3 build.py
python3 -m http.server 8000 --directory dist --bind 127.0.0.1
```

Push changes to `main`; the GitHub Actions workflow rebuilds and deploys `dist/`. Do not edit generated HTML. The site uses Source Sans 3 through Google Fonts.
