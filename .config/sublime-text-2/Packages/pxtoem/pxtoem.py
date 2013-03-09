import sublime, sublime_plugin
  
class pxtoemCommand(sublime_plugin.TextCommand):  
    def run(self, edit):  
    	view = self.view
        for region in view.sel():  
            if not region.empty():  
            	self.settings = sublime.load_settings('pxtoem.sublime-settings')
                px=self.settings.get('1em', 16)
                # Get the selected text  
                s = view.substr(region)  
                # Remove px
                s = s[:-2]
                print px
                # Convert to em
                s = float(s) / px
                print s
                # Add em
                s = str(s)+'em'
                # Replace the selection with transformed text  
                view.replace(edit, region, s)

class emtopxCommand(sublime_plugin.TextCommand):
    def run(self, edit):  
        view = self.view
        for region in view.sel():  
            if not region.empty():  
                self.settings = sublime.load_settings('pxtoem.sublime-settings')
                px=self.settings.get('1em', 16)
                # Get the selected text  
                s = view.substr(region)  
                # Remove px
                s = s[:-2]
                # Convert to em
                s = float(s) * px
                print s
                # Add em
                s = str(s)+'px'
                # Replace the selection with transformed text  
                view.replace(edit, region, s)