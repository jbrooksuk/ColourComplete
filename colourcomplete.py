import sublime, sublime_plugin

class ColourCompleteCommand(sublime_plugin.EventListener):
	colours = []

	def __init__(self, *args, **kwargs):
		self.settings = sublime.load_settings('Colours.sublime-settings')
		self.colours  = self.settings.get('colours')

	def on_query_completions(self, view, prefix, locations):
		self.completions = []

		if not view.match_selector(locations[0], 'source.css'):
			return []

		default_completions = [view.extract_completions(prefix)]
		default_completions = [(item, item) for sublist in default_completions for item in sublist if len(item) > 3]
		default_completions = list(set(default_completions))
		completions         = list(self.colours)
		completions         = [tuple(attr) for attr in self.colours]
		completions.extend(default_completions)

		return (completions)