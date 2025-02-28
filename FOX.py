
import marshal, zlib, base64
data = "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"
exec(marshal.loads(zlib.decompress(base64.b64decode(data))))
