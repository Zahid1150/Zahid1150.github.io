# Md Zahidul Islam — personal website

## Website structure

Home, Research, Projects, Publications, Experience & Education, Community & Service, and Gallery. The mobile menu appears below 1201px. The academic CV remains a separate navigation button.

The homepage features physician scheduling, learning-based routing, supply-chain simulation, a brief background, selected honors, community involvement, and gallery/contact links. Detailed project and publication content has been preserved from the latest repository version.

## Editing and building

Editable content lives in `content/*.json`. These files control the homepage, navigation/document links, education, awards, community service, and gallery albums. Retained detailed research/project/experience page bodies are in `_site/pages/`.

Run from the repository root:

```sh
python _build/build.py
python _build/check_site.py
python _build/package_site.py
```

The public deployment folder is `dist/`. Source content, build scripts, and repository metadata are not included in it. Generated HTML at the repository root is also updated so the site can still be previewed directly.

For a local preview: `python -m http.server 8765`. Open `http://localhost:8765/`.

## GitHub Pages deployment

In repository Settings → Pages → Build and deployment, choose **GitHub Actions**. The included `pages.yml` workflow rebuilds, checks, packages, and publishes the site after a push to `main`. The website retains its `https://zahid1150.github.io` address.

## Adding gallery photos manually

No CMS, Netlify account, or separate login is needed. Use your existing GitHub account.

1. Open the repository on GitHub and upload your photos to `images/gallery/` using **Add file → Upload files**. Create the folder when adding your first photo.
2. Open `content/gallery.json` and click the edit pencil.
3. Add one entry per photo using the format below. Match the image filename exactly, including capitalization. Use the same album name to group photos together.
4. Commit your changes. The included GitHub Actions workflow builds and publishes the gallery automatically once Pages is configured to use GitHub Actions.
5. Open the Gallery page after the deployment finishes.

```json
{
  "photos": [
    {
      "image": "images/gallery/your-photo.jpg",
      "alt": "Describe the people and activity visible in the photo",
      "caption": "Your photo caption",
      "album": "RUET & Bangladesh",
      "date": "2019"
    }
  ]
}
```

The entry above is an example only. Replace it with your actual filename, caption, and date. Add commas between entries, but not after the last one. Photo order follows the list order. To remove a photo from the gallery, remove its entry; deleting the image file is optional.

Upload web-sized JPEG/WebP photos, ideally under 2 MB. Images load lazily. No event photos were available in the supplied assets, so the gallery displays “Photos coming soon” until you add entries.

## Content provenance

Community roles and awards were checked against the supplied master CV and academic CV source. RUET student roles share the CV's grouped 2012–2016 period; exact per-role dates are not asserted. INFORMS Magna Cum Laude awards are explicitly chapter recognition. Existing resume/CV downloads were preserved. The homepage avoids the unverified night-shift “about half” reduction claim.

## Verification

Static checks cover local file references, anchors, unique IDs, one main landmark and one h1 per page, and content JSON. Browser checks cover all public pages at phone/tablet/desktop widths, image loading, horizontal overflow, mobile menu actions, reduced motion, gallery filtering/enlargement using a temporary fixture. No sample gallery photos are published.

`_build/browser_check.cjs` needs Playwright and Microsoft Edge; set `NODE_PATH` to an installed Playwright package location when necessary. It is a local QA helper, not part of the deployment build.

Live deployment still requires access to your GitHub repository.
