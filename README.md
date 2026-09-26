# **Prebuilt stock oplus Camera to include in custom ROM builds.**

## How to use?

1. Clone this repo to `device/oneplus/camry-camera`:
```
git clone https://github.com/diathequeen/android_device_oneplus_camry-camera.git device/oneplus/camry-camera
```
2. For the camera to work ensure that the `PRODUCT_BRAND` is OnePlus, like this `PRODUCT_BRAND := OnePlus` < (in lineage_(device-codename).mk) and that it is not overriden by any of the safetynet hacks.
3. To generate a vendor tree from this, run `./extract-files.py` in cli with a link to your device dump, just like:
```
./extract-files.py ~/blobs_dir/device_dump/
```
You can have a dump using `dumpyara` tool that unpacks partition filesystem:
```
pip install dumpyara --break-system-packages
dumpyara OTA_package.zip
```
