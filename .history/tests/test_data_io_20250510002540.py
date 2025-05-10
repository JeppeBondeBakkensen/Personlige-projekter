import io
from data_io import load_data
import pytest
import pandas as pd
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_io import load_data
# 1. Happy path: simple CSV with headers + data
def test_load_simple_csv(tmp_path):
    csv = "a,b,c\n1,2,3\n4,5,6\n"
    p = tmp_path / "simple.csv"
    p.write_text(csv)
    
    df = load_data(str(p))
    # compare to pandas.read_csv directly
    expected = pd.read_csv(str(p))
    pd.testing.assert_frame_equal(df, expected)