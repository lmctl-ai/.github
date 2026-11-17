# Build image for Linux release binaries that must run on old glibc: manylinux_2_28 (AlmaLinux 8, glibc 2.28),
# the oldest glibc a current maintained toolchain targets. Binaries that link everything but glibc statically
# get the glibc of THIS image as their floor.
ARG IMAGE=quay.io/pypa/manylinux_2_28_x86_64
FROM ${IMAGE}
ARG LMCTL_VERSION=
# glibc-static: some test suites link a fully static program to prove their linkage checks reject it.
RUN dnf install -y perl-core xz curl ca-certificates python3 make glibc-static && dnf clean all
# Node (checksum verified) to run the lmscript compiler the tests use.
RUN case "$(uname -m)" in x86_64) N=x64;; aarch64) N=arm64;; *) exit 1;; esac \
 && cd /tmp && curl -fsSLO https://nodejs.org/dist/latest-v24.x/SHASUMS256.txt \
 && F=$(grep "linux-$N.tar.xz" SHASUMS256.txt | awk '{print $2}') && curl -fsSLO "https://nodejs.org/dist/latest-v24.x/$F" \
 && grep " $F\$" SHASUMS256.txt | sha256sum --check --strict && tar -xJf "$F" -C /usr/local --strip-components=1 && rm -f "$F" SHASUMS256.txt
# The system python is 3.6; the tests use a current one. The arm64 image carries no ninja.
ENV PATH=/opt/python/cp312-cp312/bin:$PATH HOME=/tmp
RUN command -v ninja >/dev/null || python3 -m pip install --no-cache-dir ninja
RUN if [ -n "$LMCTL_VERSION" ]; then npm install --global "@lmctl-ai/lmctl@$LMCTL_VERSION"; fi
WORKDIR /work
