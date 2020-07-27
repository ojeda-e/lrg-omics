import pandas as pd

from lrg_omics.metabolomics.common import metadata_from_worklist, metadata_from_filename


class Test_metadata_from_filename():
    def test__file_with_bi_nbr(self):
        fn = '2020_05_11RG_HILICNeg15S_Col002_LSARP_SA001_RPT001_BI_16_0076.mzXML'
        actual = metadata_from_filename(fn)
        data = {'BI_NBR': 'BI_16_0076', 
                'DATE': '2020-05-11', 
                'RPT': 1, 
                'PLATE_ID': 'SA001',
                'SAMPLE_TYPE': 'BI',
                'MS_MODE': 'Neg'}
        expected = pd.DataFrame(data, index=[0])
        assert actual.equals(expected), f'\nExpected:\n {expected}\nReceived:\n {actual}'

    def test__file_with_standard(self):
        fn = '2020_05_11RG_HILICPos15S_Col002_LSARP_SA001_RPT001_Standard-50nm.mzXML'
        actual = metadata_from_filename(fn)
        data = {'BI_NBR': 'nan', 
                'DATE': '2020-05-11', 
                'RPT': 1, 
                'PLATE_ID': 'SA001',
                'SAMPLE_TYPE': 'ST',
                'MS_MODE': 'Pos'}
        expected = pd.DataFrame(data, index=[0])
        assert actual.equals(expected), f'\nExpected:\n {expected}\nReceived:\n {actual}'
    
    def test__file_with_qc_sample(self):
        fn = '2020_05_11RG_HILICPos15S_Col001_LSARP_SA001_RPT001_QC02_SA001.mzXML'
        actual = metadata_from_filename(fn)
        data = {'BI_NBR': 'nan', 
                'DATE': '2020-05-11', 
                'RPT': 1, 
                'PLATE_ID': 'SA001',
                'SAMPLE_TYPE': 'QC',
                'MS_MODE': 'Pos'}
        expected = pd.DataFrame(data, index=[0])
        assert actual.equals(expected), f'\nExpected:\n {expected}\nReceived:\n {actual}'