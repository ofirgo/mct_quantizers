# Copyright 2023 Sony Semiconductor Israel, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import unittest
import sys

from tests.compatibility_tests.keras_comp_tests.base_weights_compatibility_test import BaseWeightsQuantizerLoadAndCompareTest
from tests.compatibility_tests.keras_comp_tests.compatibility_load_model_test import \
    WeightsPOTQuantizerLoadAndCompareTest, WeightsSymmetricQuantizerLoadAndCompareTest, \
    WeightsUniformQuantizerLoadAndCompareTest, WeightsPOTLutQuantizerLoadAndCompareTest, \
    WeightsSymmetricLutQuantizerLoadAndCompareTest

if __name__ == '__main__':
    mct_quantizers_version = sys.argv[1]
    suiteList = []
    test_loader = unittest.TestLoader()

    BaseWeightsQuantizerLoadAndCompareTest.SAVED_VERSION = mct_quantizers_version

    suiteList.append(test_loader.loadTestsFromTestCase(WeightsPOTQuantizerLoadAndCompareTest))
    suiteList.append(test_loader.loadTestsFromTestCase(WeightsSymmetricQuantizerLoadAndCompareTest))
    suiteList.append(test_loader.loadTestsFromTestCase(WeightsUniformQuantizerLoadAndCompareTest))
    suiteList.append(test_loader.loadTestsFromTestCase(WeightsPOTLutQuantizerLoadAndCompareTest))
    suiteList.append(test_loader.loadTestsFromTestCase(WeightsSymmetricLutQuantizerLoadAndCompareTest))

    keras_load_models_suite = unittest.TestSuite(suiteList)

    test_result = unittest.TextTestRunner(verbosity=0).run(keras_load_models_suite)

    # Exit with a non-zero code if tests failed
    if not test_result.wasSuccessful():
        print(f"Encountered an error during load model tests, "
              f"for models that were saved with version {mct_quantizers_version}")
        sys.exit(1)
