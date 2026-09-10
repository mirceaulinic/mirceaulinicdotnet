# mirceaulinic.net — Hugo + PaperMod

Modernized version of the original Mircea Ulinic technical blog.

## Local setup

This repository intentionally does **not** vendor or fork PaperMod. Add it as a Git submodule:

```bash
git submodule add --depth 1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

Install Hugo Extended, then:

```bash
hugo server -D
```

Open the local address printed by Hugo.

## Migration notes

- Original post URLs are preserved as `/YYYY-MM-DD-slug/`.
- Legacy images remain under `/img/` so existing image references can continue to work.
- Old Beautiful Jekyll-specific front matter was converted to Hugo/PaperMod front matter.
- Legacy Jekyll/Ruby configuration, plugins, and social configuration are intentionally not carried over.
- Disqus and the old Google Analytics UA property are not migrated.
- PaperMod is kept upstream; site-specific changes belong in `layouts/` and `assets/`.

## Deployment

The included GitHub Actions workflow builds Hugo and deploys to GitHub Pages.

For the custom domain, keep a `CNAME` containing:

```text
mirceaulinic.net
```

Then configure the repository's Pages source to **GitHub Actions**.
