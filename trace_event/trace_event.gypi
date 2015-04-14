# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
{
  'variables': {
    'trace_event_sources' : [
      'trace_event/memory_allocator_attributes.h',
      'trace_event/memory_allocator_dump.cc',
      'trace_event/memory_allocator_dump.h',
      'trace_event/memory_dump_manager.cc',
      'trace_event/memory_dump_manager.h',
      'trace_event/memory_dump_provider.cc',
      'trace_event/memory_dump_provider.h',
      'trace_event/memory_dump_request_args.h',
      'trace_event/process_memory_dump.cc',
      'trace_event/process_memory_dump.h',
      'trace_event/process_memory_maps.cc',
      'trace_event/process_memory_maps.h',
      'trace_event/process_memory_maps_dump_provider.cc',
      'trace_event/process_memory_maps_dump_provider.h',
      'trace_event/process_memory_totals.cc',
      'trace_event/process_memory_totals.h',
      'trace_event/process_memory_totals_dump_provider.cc',
      'trace_event/process_memory_totals_dump_provider.h',
      'trace_event/trace_event.h',
      'trace_event/trace_event_android.cc',
      'trace_event/trace_event_argument.cc',
      'trace_event/trace_event_argument.h',
      'trace_event/trace_event_impl.cc',
      'trace_event/trace_event_impl.h',
      'trace_event/trace_event_impl_constants.cc',
      'trace_event/trace_event_memory.cc',
      'trace_event/trace_event_memory.h',
      'trace_event/trace_event_synthetic_delay.cc',
      'trace_event/trace_event_synthetic_delay.h',
      'trace_event/trace_event_system_stats_monitor.cc',
      'trace_event/trace_event_system_stats_monitor.h',
      'trace_event/trace_event_win.cc',
      'trace_event/trace_event_win.h',
    ],
    'trace_event_test_sources' : [
      'trace_event/memory_allocator_dump_unittest.cc',
      'trace_event/memory_dump_manager_unittest.cc',
      'trace_event/process_memory_maps_dump_provider_unittest.cc',
      'trace_event/process_memory_totals_dump_provider_unittest.cc',
      'trace_event/trace_event_argument_unittest.cc',
      'trace_event/trace_event_memory_unittest.cc',
      'trace_event/trace_event_synthetic_delay_unittest.cc',
      'trace_event/trace_event_system_stats_monitor_unittest.cc',
      'trace_event/trace_event_unittest.cc',
      'trace_event/trace_event_win_unittest.cc',
    ],
  },
}
