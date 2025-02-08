# Replace /path/to/rocky-linux-base.iso with the original Rocky Linux ISO path.
rm -rf output
mkdir -p output

#sudo mkksiso minimal-rt-kde.ks Rocky-9.5-x86_64-minimal.iso output/kde-rt.iso
#exit 0


livemedia-creator --ks ../kickstart/minimal-rt-mate.ks \
  --no-virt \
  --resultdir output/rocky-rt-iso2/ \
  --project="Rocky Linux Mate RT" \
  --make-iso \
  --volid Rocky-MATE-RT \
  --iso-only \
  --iso-name Rocky-9.5-x86_64-minimal.iso \
  --releasever=9 \
  --nomacboot  # This option is important to set, mkfs.hfsplus is not available
