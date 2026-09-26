# **Prebuilt stock oplus Camera to include in custom ROM builds.**

## How to use?

1. Clone this repo to `device/oneplus/camry-camera`:
```
git clone https://github.com/diathequeen/android_device_oneplus_camry-camera.git device/oneplus/camry-camera
```
2. For the camera to work ensure that the `PRODUCT_BRAND` is OnePlus, like this `PRODUCT_BRAND := OnePlus` < (in lineage_<device>.mk) and that it is not overriden by any of the safetynet hacks.
