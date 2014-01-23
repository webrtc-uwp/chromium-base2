// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "base/rand_util.h"

#include <stdlib.h>

#include "base/basictypes.h"
#include "base/logging.h"

namespace {

uint32 RandUint32() {
  uint32 number;
  CHECK_EQ(rand_s(&number), 0);
  return number;
}

}  // namespace

namespace base {

// NOTE: This function must be cryptographically secure. http://crbug.com/140076
uint64 RandUint64() {
  uint32 first_half = RandUint32();
  uint32 second_half = RandUint32();
  return (static_cast<uint64>(first_half) << 32) + second_half;
}

void RandBytes(void* output, size_t output_length) {
  uint64 random_int;
  const size_t random_int_size = sizeof(random_int);
  for (size_t i = 0; i < output_length; i += random_int_size) {
    random_int = base::RandUint64();
    const size_t copy_count = std::min(output_length - i, random_int_size);
    memcpy(((uint8*)output) + i, &random_int, copy_count);
  }
}

}  // namespace base
