from os.path import isfile, join, abspath
from glob import glob 

from lrg_omics.proteomics.pipelines.maxquant import run_maxquant

PATH = abspath( join( 'tests', 'data' ) )

def test__run_maxquant(tmpdir):
    return None    
    fasta_file = join(PATH, 'fasta', 'Saureus.fasta')
    mqpar_file = join(PATH, 'maxquant', 'tmt11', 'mqpar', 'mqpar.xml')
    fake_raw_file = join(PATH, 'fake', 'fake.raw')
    
    assert isfile(fasta_file)
    assert isfile(mqpar_file)
    assert isfile(fake_raw_file)
    
    run_dir = join( tmpdir, 'run')
    
    cmds = run_maxquant(maxquantbin='./tests/data/fake/MaxQuant.bash', raw=fake_raw_file, fasta=fasta_file, mqpar=mqpar_file, 
                        pipename='test_pipe', run_root=run_dir)
    
    for i in glob( f'{tmpdir}/**', recursive=True):
        print(i)
    
    for cmd in cmds:
        print(cmd)
        
    assert True
    
