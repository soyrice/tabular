<h1>Basic Field Calculations <small> for ArcGIS&reg;</small></h1>![license mit](https://img.shields.io/packagist/l/doctrine/orm.svg) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/soyrice/tabular/issues)

## Get started

Tabular is an unofficial, interactive manual for the [Calculate Field](http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/calculate-field.htm) tool in ArcGIS Desktop. Tabular is designed for new GIS and Python users to learn scripting for spatial analysis.

You can copy-and-paste Python expressions into ArcGIS, navigate through the tool with screenshots, and test your code in Python sandboxes. Or you can download [the cheat sheet]().

## Edit some text
---

### Find characters

Goal | <h7>Code snippet<h8>------------------------------------------------------------------</h8><h7> |
--- | ---
Return the first character | <details><summary>`!fieldname![0]`</summary><img src="/images/1.png";></details> |
Return the first through third characters | <details><summary>`!fieldname![0:3]`</summary><img src="/images/2.png";></details> |
Return the second-to-last character | <details><summary>`!fieldname![-2]`</summary><img src="/images/3.png";></details> |

### Remove characters 

Goal | Code snippet |
--- | ---
Remove all whitespace | <details><summary>`!fieldname!.rstrip()`</summary><img src="/images/4.png";></details> |
Swap certain words | <details><summary>`!fieldname!.replace("value", "New Value")`</summary><img src="/images/5.png";></details> |
Remove all non-alphanumeric characters | <details><summary>`‘’.join(ch for ch in !fieldname! if ch.isalnum())`</summary><img src="/images/6.png";></details> |
Return `<Null>` | <details><summary>`"None"`</summary><img src="/images/7.png";></details> |

### Format the string
Goal | <h7>Code snippet<h8>-----------------------------------------------</h8><h7> |
--- | ---
Capitalize the string | <details><summary>`!fieldname!.capitalize()`</summary><img src="/images/8.png";></details> |
Convert the string to lowercase | <details><summary>`!fieldname!.lower()`</summary><img src="/images/9.png";></details> |
Convert the string to all caps | <details><summary>`!fieldname!.upper()`</summary><img src="/images/10.png";></details> |

## Do some math
---

### Add and subtract

Goal | <h7>Code snippet<h8>--------------------------------------------</h8><h7> |
--- | ---
Add 5 to the field value | <details><summary>`!fieldname! + 5`</summary><img src="/images/11.png";></details> |
Subtract 6 from the field value | <details><summary>`!fieldname! - 6`</summary><img src="/images/12.png";></details> |

### Multiply and divide

Goal<h8>--------------------------------------</h8> | <h7>Code snippet<h8>--------------------------------------------</h8><h7> |
--- | ---
Multiply by 2 | <details><summary>`!fieldname! * 2`</summary><img src="/images/13.png";></details> |
Divide by 3 | <details><summary>`!fieldname! / 3`</summary><img src="/images/14.png";></details> |

### Execute simple functions
In the Field Calculator, you can execute <h9><span style="background-color: #e3d9de">anything listed under [Functions:](http://teachmegis.com/tiptricks/Editing%20Tables%20with%20the%20Field%20Calculator.pdf)</span> or <span style="background-color: lightyellow">any [built-in Python functions](https://docs.python.org/2/library/functions.html)</span>.

Goal | <h7>Code snippet<h8>---------------------------------</h8><h7> |
--- | ---
<span style="background-color: #e3d9de">Calculate the logarithm</span> | <details><summary>`math.log(!fieldname!)`</summary><img src="/images/15.png";></details> |
<span style="background-color: lightyellow">Round to 2 decimal places</span> | <details><summary>`round(!fieldname!, 2)`</summary><img src="/images/16.png";></details> |

## Deal with geometries
---

### Find feature extents

Goal | <h7>Code snippet<h8>--------------------------------------------</h8><h7> |
--- | ---
Find the most extreme longitude | <details><summary>`!shape.extent.XMax!`</summary><img src="/images/17.png";></details> |
Find the most extreme latitude | <details><summary>`!shape.extent.YMax!`</summary><img src="/images/18.png";></details> |

### Calculate line lengths

Goal | <h7>Code snippet<h8>----------------------------------------------------------</h8><h7> |
--- | ---
Calculate feature length in map units | <details><summary>`!shape.length!`</summary><img src="/images/19.png";></details> |
Calculate feature length in feet | <details><summary>`!shape.length@feet!`</summary><img src="/images/20.png";></details> |
Calculate feature length in geodesic feet | <details><summary>`!shape.length@Geodesicfeet!`</summary><img src="/images/21.png";></details> |

### Compute shape areas
Goal | <h7>Code snippet<h8>---------------------------------------------------------------------</h8><h7> |
--- | ---
Calculate feature area in map units | <details><summary>`!shape.area!`</summary><img src="/images/22.png";></details> |
Calculate feature area in square feet | <details><summary>`!shape.area@squarefeet!`</summary><img src="/images/23.png";></details> |
Calculate feature area in geodesic square feet | <details><summary>`!shape.area@Geodesicsquarefeet!`</summary><img src="/images/24.png";></details> |

## Further reading

You can perform more advanced calculations with the [code block](http://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field-examples.htm#ESRI_SECTION1_DF13F7EE4AF345CAAA46C1CFA2F7BFE1) in the Field Calculator. Check out [some](http://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field-examples.htm#ESRI_SECTION1_11EAB368A53B4D1C9618A58A1B09F9D0) [examples](http://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field-examples.htm#ESRI_SECTION1_F3F8CD77A9F647ABBA678A76ADB86E15) in the official Esri documentation.

Shitij Mehta [wrote a blog series](https://blogs.esri.com/esri/arcgis/2011/06/06/modelbuilderifthenelse1/) on if-then-else statements that you can apply to field calculations.

David Verbyla made [a video](https://www.youtube.com/watch?v=gvB4GjLcEcg) on Python functions for the Field Calculator.




