# ColourComplete

A **work in progress** Sublime Text plugin to complete custom CSS colour names with the hex value.

The idea came about whilst at work after we all gave up trying to remember the hex value for the [Flat UI Colours](http://flatuicolors.com).

# Setup
`Colours.sublime-settings` contains a `colours` key which is an array of colours:

```json
{
    "colours": [
        ["turquoise\tFlat UI", "#1abc9c"],
        ["emerland\tFlat UI", "#2ecc71"],
        ["peter-river\tFlat UI", "#3498db"],
        ["amethyst\tFlat UI", "#9b59b6"],
        ["wet-asphalt\tFlat UI", "#34495e"],
        ["green-sea\tFlat UI", "#16a085"],
        ["nephritis\tFlat UI", "#27ae60"],
        ["belize-hole\tFlat UI", "#2980b9"],
        ["wisteria\tFlat UI", "#8e44ad"],
        ["midnight-blue\tFlat UI", "#2c3e50"],
        ["sun-flower\tFlat UI", "#f1c40f"],
        ["carrot\tFlat UI", "#e67e22"],
        ["alizarin\tFlat UI", "#e74c3c"],
        ["clouds\tFlat UI", "#ecf0f1"],
        ["concrete\tFlat UI", "#95a5a6"],
        ["orange\tFlat UI", "#f39c12"],
        ["pumpkin\tFlat UI", "#d35400"],
        ["pomegranate\tFlat UI", "#c0392b"],
        ["silver\tFlat UI", "#bdc3c7"],
        ["asbestos\tFlat UI", "#7f8c8d"]
    ]
}
```

For anyone who doesn't know how Sublime completions work, the `\tFlat UI` will display on the right hand side of the completions list.

Now when you type `alizarin` Sublime will auto complete to `#e74c3c`. Simples!

# Bugs

1. Adding a `Colours.sublime-settings` to your `User` folder will overwrite all existing default colours.
2. It'll only work in `source.css` scope. I need to add SCSS/SASS/LESS as well.

# License
[MIT](http://jbrooksuk.mit-license.org)