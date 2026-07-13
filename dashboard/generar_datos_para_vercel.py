#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copiar datos.js a public/
"""

import shutil
import os

print("Copiando datos.js a public/...")

try:
    shutil.copy2('datos.js', 'public/datos.js')
    
    size_mb = os.path.getsize('public/datos.js') / 1024 / 1024
    size_orig_mb = os.path.getsize('datos.js') / 1024 / 1024
    
    print(f"✓ Copia completada")
    print(f"  Original: {size_orig_mb:.2f} MB")
    print(f"  Copia: {size_mb:.2f} MB")
except Exception as e:
    print(f"Error: {e}")
