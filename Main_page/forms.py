from django import forms

BD_choices = [('8','8'), ('10','10')]
Res_choices_horizontal = [('640','640'), ('480','480'),('384','384'),('256','256'),('128','128'), ('80','80'), ('16','16'), ('8','8')]
Res_choices_vertical = [('640','640'), ('480','480'),('384','384'),('256','256'),('128','128'), ('80','80'), ('16','16'), ('8','8')]
SI_choices = [('5','5'), ('10','10')]
TC_choices = [('A','A'), ('B','B')]


class S200Form(forms.Form):
	Bit_Depth = forms.CharField(label = 'Enter Bit Depth', widget=forms.widgets.Select(choices=BD_choices))
	Resolution_horizontal = forms.CharField(label = 'Enter Horizontal Resolution', widget=forms.widgets.Select(choices=Res_choices_horizontal))
	Resolution_vertical = forms.CharField(label = 'Enter Vertical Resolution', widget=forms.widgets.Select(choices=Res_choices_vertical))
	FPS = forms.CharField(label = 'Enter FPS')

class PicoForm(forms.Form):
	Sampling_interval = forms.CharField(label = 'Enter sampling interval in nanoseconds', widget=forms.widgets.Select(choices=SI_choices))
	Trigger_channel = forms.CharField(label = 'Enter trigger channel', widget=forms.widgets.Select(choices=TC_choices))
	Downsampling_ratio = forms.CharField(label = 'Enter Downsampling ratio')

class Storag_loc(forms.Form):
	location = forms.CharField(label = 'Enter location')
	build_name = forms.CharField(label = 'Enter build name')