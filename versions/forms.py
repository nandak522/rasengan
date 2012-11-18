import re
from django import forms
from django.core.exceptions import ValidationError

class VersionsForm(forms.Form):
    versions = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows':15, 'cols':20}))

    def clean_versions(self):
        '''Validate Each version submitted if its following pkgname == version syntax'''
        versions = self.cleaned_data.get('versions')
        versions_info = []
        for version in versions.split('\n'):
            matches = re.match(r'(\w+)[\s]*={1,2}[\s]*(\d[.\d]*[\w]*)', version)
            if matches:
                versions_info.append(matches.groups())
            else:
                raise ValidationError('Wrong Version Format for: %s' % version)
        versions_info.sort()
        return versions_info
