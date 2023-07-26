# -*- coding: utf-8 -*-
from celery import shared_task
from contextlib import contextmanager
from django.core.cache import cache
import time


@contextmanager
def memcache_lock(lock_id, oid, lock_expire=5 * 60 * 60):
    """
    Memcache-based lock
    :param lock_id: the lock id
    :param oid: the owner id
    :param lock_expire: the lock expiration time
    """
    timeout_at = time.monotonic() + lock_expire - 3
    # cache.add fails if the key already exists
    status = cache.add(lock_id, oid, lock_expire)
    try:
        yield status
    finally:
        if time.monotonic() < timeout_at and status:
            cache.delete(lock_id)


@shared_task(bind=True, name='test_task', content_encoding='utf-8')
def test_task(self) -> dict:
    return {'result': 'Привет! Я тестовая задача и я работаю!'}
