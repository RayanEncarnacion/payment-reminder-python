from django import forms
from .models import Client
from django.forms.widgets import Select, Widget, TextInput, NumberInput

class CustomWidget():
    widget: Widget = None;
    
    def __init__(self, widget: Widget = TextInput, **kwargs): 
        self.widget = widget();
        self.widget.__init__(attrs=kwargs)
    
    def get(self):
        return self.widget
    
class FormControl(forms.Form):
    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        
        """ Add the 'form-control' class to all visible fields, except for selects """
        for visible in self.visible_fields():
            input_class = 'form-select' if type(visible.field.widget) == Select else "form-control"
            visible.field.widget.attrs['class'] = input_class
            
def get_active_clients():
    return Client.objects.filter(active__exact=True, deleted__exact=False)
class CreateClient(FormControl):
    name = forms.CharField(max_length=100, required=True, strip=True)
    email = forms.EmailField(required=True)
                                                                                
class CreateProject(FormControl):
    name = forms.CharField(max_length=100, 
                           required=True, 
                           strip=True, 
                           widget=CustomWidget(placeholder="Google").get())
    
    amount = forms.FloatField(step_size=0.1, 
                              required=True, 
                              widget=CustomWidget(NumberInput, placeholder="1000.00").get())
    
    client = forms.ModelChoiceField(queryset=get_active_clients(), empty_label="Choose a client", required=True)