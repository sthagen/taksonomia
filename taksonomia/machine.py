"""Taxonomy (Finnish: taksonomia) guided by conventions of a folder tree (implementation)."""
import datetime as dti
import os
import platform
import uuid
from typing import no_type_check

import psutil  # type: ignore
from cpuinfo import get_cpu_info  # type: ignore

from taksonomia import TS_FORMAT


@no_type_check
class Machine:
    """Auxiliary context and performance information provider."""

    def __init__(self, path_selector: str, pid: int) -> None:
        """Construct a machine instance pinned on a process id and a path."""
        self.path_selector = path_selector
        self.pid = pid

    @no_type_check
    def perf(self):
        """Some random information from machine performance measures."""
        p = psutil.Process(self.pid)
        cpts = p.cpu_times()
        cpts_union_attrs = ('children_system', 'children_user', 'system', 'user')
        mfi = p.memory_full_info()
        mfi_union_attrs = ('pageins', 'pfaults', 'rss', 'uss', 'vms')
        threads = p.threads()
        thr_union_attrs = ('id', 'system_time', 'user_time')
        ctxs = p.num_ctx_switches()
        ctxs_union_attrs = ('involuntary', 'voluntary')
        return {
            'name': p.name() if hasattr(p, 'name') else None,
            'status': p.status() if hasattr(p, 'status') else None,
            'create_time': dti.datetime.fromtimestamp(p.create_time(), dti.timezone.utc).strftime(TS_FORMAT),
            'username': p.username() if hasattr(p, 'username') else None,
            'cpu_times': {aspect: getattr(cpts, aspect, None) for aspect in cpts_union_attrs},
            'memory_full_info': {aspect: getattr(mfi, aspect, None) for aspect in mfi_union_attrs},
            'memory_percent': p.memory_percent() if hasattr(p, 'memory_percent') else None,
            'num_threads': p.num_threads() if hasattr(p, 'num_threads') else None,
            'threads': [{aspect: getattr(thr, aspect, None) for aspect in thr_union_attrs} for thr in threads],
            'num_fds': p.num_fds() if hasattr(p, 'num_fds') else None,
            'num_ctx_switches': {aspect: getattr(ctxs, aspect, None) for aspect in ctxs_union_attrs},
        }

    @no_type_check
    def context(self):
        """Some random information from machine context."""
        swa = psutil.swap_memory()
        swa_union_attrs = ('free', 'percent', 'sin', 'sout', 'total', 'used')
        vim = psutil.virtual_memory()
        vim_union_attrs = (
            'active',
            'available',
            'buffers',
            'cached',
            'free',
            'inactive',
            'percent',
            'shared',
            'slab',
            'total',
            'used',
            'wired',
        )
        dic = psutil.disk_io_counters(perdisk=False)
        dic_union_attrs = ('read_bytes', 'read_count', 'read_time', 'write_bytes', 'write_count', 'write_time')
        du = psutil.disk_usage(self.path_selector)
        du_union_attrs = ('free', 'percent', 'total', 'used')
        dpas = psutil.disk_partitions()
        dpa_union_attrs = ('device', 'fstype', 'maxfile', 'maxpath', 'mountpoint')
        partitions = []
        for dpa in dpas:
            partitions.append(
                {
                    **{aspect: getattr(dpa, aspect, None) for aspect in dpa_union_attrs},
                    'opts': dpa.opts.split(',') if hasattr(dpa, 'opts') else None,
                }
            )

        return {
            'node_identifier': str(uuid.uuid3(uuid.NAMESPACE_DNS, platform.node())),
            'pid': os.getpid(),
            'ppid': os.getppid(),
            'boottime': dti.datetime.fromtimestamp(psutil.boot_time(), dti.timezone.utc).strftime(TS_FORMAT),
            'cpu_info': {**get_cpu_info()},
            'memory': {
                'swap': {aspect: getattr(swa, aspect, None) for aspect in swa_union_attrs},
                'virtual': {aspect: getattr(vim, aspect, None) for aspect in vim_union_attrs},
            },
            'disks': {
                'counters_combined': {aspect: getattr(dic, aspect, None) for aspect in dic_union_attrs},
                'partitions': partitions,
                'path_selector': self.path_selector,
                'usage': {aspect: getattr(du, aspect, None) for aspect in du_union_attrs},
            },
        }
