# XPath

XPath is a syntax for selecting elements and context from XML documents. It works really well on HTML, and similarly to CSS selectors.

Examples

```xpath
//elementName[contains(@attribute, 'Some Value')]
//elementName[contains(text(), 'Some Text')]
//a[contains(@id='my-link')]
```

## XPath Axes 

- https://www.w3schools.com/xml/xpath_axes.asp
- https://stackoverflow.com/questions/28237694/xpath-get-parent-node-from-child-node

### Select Nth of selection

Index of elements begins at `1`, instead of `0`

```xpath
Select 2nd element
//*[contains(@attribute, 'Some Value')][2]
```

### Parent Element 

Add `/parent::elementName` to the end of the selector

```xpath
//elementName[contains(@attribute, 'Some Value')]/parent::parentElementName
//*[contains(@attribute, 'Some Value')]/parent::*
```