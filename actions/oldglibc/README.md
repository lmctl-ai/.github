# oldglibc

Build Linux release binaries that run on old glibc. Inside a `manylinux_2_28` image (AlmaLinux 8, glibc 2.28) it
runs your command with the workspace mounted at its host path, then fails the job if a binary you name needs a
newer glibc. Build-time only: nothing from here ships in your binary.

```yaml
- uses: lmctl-ai/.github/actions/oldglibc@<commit sha>   # pin a commit
  with:
    lmctl-version: 0.2.482          # optional: puts lmscript in the image
    env: GITHUB_TOKEN               # names of variables to pass in, one per line
    run: ./test.sh
    check: build/mytool             # ELF paths or globs to gate
    max-glibc: '2.28'
```

Pin a full commit sha, not a branch. The image runs your command as the runner's user with `HOME=/tmp`.
The system Python in the image is 3.6; Python 3.12 is first on PATH.
