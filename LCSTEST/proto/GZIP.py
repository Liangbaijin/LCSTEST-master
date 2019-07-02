# -*- coding: utf-8 -*-
import gzip
import io

class Gzip():
    # 压缩序列化数据流#
    def gzip_compress(raw_data):
        buf = io.BytesIO()
        f = gzip.GzipFile(mode='wb', fileobj=buf)
        try:
            f.write(raw_data)
        finally:
            f.close()
        return buf.getvalue()

    # 解压缩序列化数据流#
    def gzip_uncompress(c_data):
        buf = io.BytesIO(c_data)
        f = gzip.GzipFile(mode='rb', fileobj=buf)
        try:
            r_data = f.read()
        finally:
            f.close()
        return r_data
