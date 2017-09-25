## Test your Python expressions
Try field calculations without editing your data. Use the interactive console below to input a string or numeric field value. Then enter a field calculation to see what happens.

### Play in the sandbox
<iframe src="https://trinket.io/embed/python/516a991bc4?outputOnly=true&start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Transition to ArcGIS
After you use the sandbox, bring your skills to the Field Calculator. But be careful: field calculations will permenently alter your data. It's good practice to have a back-up copy and perform all field calculations in a [brand new field](desktop.arcgis.com/en/arcmap/10.3/manage-data/tables/adding-fields.htm).

You can test your code in 'main.py' before using the Field Calculator. Press the <img src="/images/play.png";> play button to try your expression.

<iframe src="https://trinket.io/embed/python/cd51166fa2?start=result" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

<i class="fa fa-pencil-square-o" aria-hidden="true"></i> _Note:_ 
The sandbox supports Python expressions, but the Field Calculator in ArcMap also supports [VB Script](http://support.esri.com/en/technical-article/000008920). In ArcGIS Pro, the Calculator Field tool supports Python, VBA, and [Arcade](https://developers.arcgis.com/arcade/) expressions. 

### Test Python code blocks
The Calculate Field tool supports [logical](http://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field-examples.htm#ESRI_SECTION1_11EAB368A53B4D1C9618A58A1B09F9D0) and [accumulative](http://pro.arcgis.com/en/pro-app/tool-reference/data-management/calculate-field-examples.htm#ESRI_SECTION1_F3F8CD77A9F647ABBA678A76ADB86E15) functions, which are common advanced techniques. Experiment with the examples in `logical.py` and `accumulate.py` above.

### Learn more about Python
Python is the language of GIS. If you can do it with Python, you can do it in the Field Calculator. Check out these resources to develop your Python skills and learn more about Python scripting for spatial analysis.

Time commitment | Resource |
--- | ---
Least involved | <span style="background-color: #FFFCFC">Download an Esri [cheat sheet](chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://www.esri.com/news/arcuser/0507/files/pythonscript.pdf) of advanced logial functions for the Field Calculator</span> |
 <span style="color: transparent">-</span>| <span style="background-color: #FFEEED">Review the [the offical Python docs](https://docs.python.org/3/) when you know of a Python tool but want to learn how to use it</span>
 <span style="color: transparent">-</span>| <span style="background-color: #fbd5d4">Check out [Python for ArcGIS](https://www.youtube.com/channel/UCjGzNLUkTOFzWdD_5MzNIqg/videos), a free YouTube series from the University of Alaska</span>
 <span style="color: transparent">-</span>| <span style="background-color: #D89F9D; color: white">Try out the exercises in Paul Zandbergen's how-to book, <a href="http://esripress.esri.com/bookResources/index.cfm?event=catalog.book&id=9/" style="color: #A9CDE9">Python Scripting for ArcGIS</span>
 <span style="color: transparent">-</span>| <span style="background-color: #B66D6B; color: white">Dive into Python scripting for spatial analysis with the lessons and tutorials in <a href="https://www.esri.com/training/catalog/57630436851d31e02a43f13c/python-for-everyone/" style="color: #A9CDE9">Python for Everyone</a>, a free training by Esri</span>
Most involved | <span style="background-color: #A96260; color: white">Learn Python from scratch with interactive tutorials on <a href="https://www.codecademy.com/learn/learn-python" style="color: #A9CDE9">Codeacademy</a></span>