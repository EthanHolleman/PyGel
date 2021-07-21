from typing import Type
from pydna.gel import Gel
from pathlib import Path
import sys
from pydna.dseq import Dseq
from pydna.readers import read

class PyGel(Gel):

    def __init__(self, samples, cutters, output_path, *args, **kwargs):
        self.output_path = output_path
        self.user_samples = samples
        self.cutters = cutters
        super().__init__(self.user_samples, *args, **kwargs)
    
    @property
    def user_samples(self):
        return self._samples
    
    @user_samples.setter
    def user_samples(self, new_samples):
        samples = []
        for each_sample in new_samples:
            if isinstance(each_sample, str) or isinstance(each_sample, Path):
                each_sample = Path(each_sample)
                if not each_sample.is_file():
                    raise FileNotFoundError(f'{each_sample} not found!')
                else:
                    samples.append(each_sample)
            else:
                raise TypeError(f'Sample {each_sample} type {type(each_sample)} \
                is not a string or Path!')
        self._samples = samples

    @property
    def output_path(self):
        return self._output_path
    
    @output_path.setter
    def output_path(self, new_path):
        if isinstance(new_path, str) or isinstance(new_path, Path):
            new_path = Path(new_path)
            if not new_path.parent.is_dir():
                new_path.mkdir(parents=True, exist_ok=True)
            
            self.output_path = new_path
        else:
            raise TypeError('output_path must be a string or a Path instance!')

    def unique_digest(self):
        '''Digest each sample so that unique fragment lengths are produced.
        '''
        pass

    def run(self):
        gel_pic = super().run(plot=True)
        gel_pic.savefig(str(self.output_path), dpi=300)
    

