import os
from subprocess import check_output, CalledProcessError


class SassRunner(object):
    """Base class for Sass runners"""
    spec_root = 'repos/sass-spec-master/spec/'
    base_output_dir = 'site/results/%s/'

    @property
    def bin(self):
        raise NotImplemented()

    @property
    def name(self):
        raise NotImplemented()

    @property
    def output_dir(self):
        return self.base_output_dir % self.name

    def output(self, spec):
        """ Returns filename to put compiled css """
        output = self.output_dir + spec.replace(self.spec_root, '')
        self._create_dir(output.replace('input.scss', ''))
        return output.replace('input.scss', 'output.css')

    def run(self, spec):
        """ Implement in subclass. Output compiled css to self.output_dir """
        try:
            check_output([self.bin, spec, self.output(spec)])
        except CalledProcessError as e:
            print(e.output)

    def _create_dir(self, path):
        try:
            os.makedirs(path)
        except Exception:
            pass
