#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [

]

blob_fixups: blob_fixups_user_type = {
    'product/etc/permissions/com.oplus.camera.unit.sdk_product.xml': blob_fixup()
        .regex_replace(r'\?\s+xml', '?xml'),
}  # fmt: skip

module = ExtractUtilsModule(
    'camera',
    'oneplus',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
