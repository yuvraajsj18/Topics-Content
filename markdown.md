## 1
# CSS Cursor

## Overview

![](My New Scaler URL)



In CSS, the cursor property provides an easy way to adjust the shape and size of the cursor. This property determines the appearance of the cursor when it hovers over an element.

There are multiple cursor shapes available, such as the pointer or resize shape, and you can customize them to suit your needs.

## Scope of Article
* This article explains cursor in CSS
* How you can use Cursor Property in CSS
* All properties associated with cursor in CSS
* Syntax of Cursor property
* Browser Support of Cursor

## Cursor in CSS
CSS enables us to alter the appearance of the mouse cursor on web pages through the cursor property. This property specifies how the cursor will appear when hovering over an element, which can be a div box or the entire HTML page.

Using the cursor property, you can adjust the size and shape of the cursor. There are numerous built-in cursor types available, or you can create your own custom cursor shape with CSS.

## Syntax of cursor
Using cursor property is easy in HTML. You can use the in-built cursor keyword to change the cursor type on your screen. The cursor keyword takes a value that will define the cursor shape. 
#### Syntax
```
element tag/id/class{
    cursor : value
}
```

> **_NOTE:_**  The element tag/id/ value represents the element on which you wish to display the cursor shape. 

There are several in-built keywords value that you can use. You can refer the table given in keywords section for information on in-built cursor shapes and their values.

![cat image](My New Scaler URL)

### Cursor in CSS using url
If you want to have a custome shape url, then you can do it as well. For that, you would require to input a link which points to the image you want to set as a pointer shape. In addition to that, you also require to give a default value from the reserved keyword value. In case the browser is unable to block your cursor image from loading, then your cursor keyword will fallback to the reserved keyword values.

If you have multiple cursor images, then you can use them as well. You can use multiple url in a single cursor property. However, the browser will only use one of them. It was start evaluating the url from left to right. The first image that loads correctly will be used as a cursor shape for that element.
#### Syntax
```
element tag/id/class{
    cursor : url(Link to first image) url(Link to second image) reserved keyword value;
}
```

### ```<x>``` and ```<y>``` attributes for Cursor in CSS
The x and y coordinates are optional values that you can provide. The x and y parameters defined the precise position of the cursor that is being pointed to. For example, if x and y values are set to 0 and 0, then the x and y coordinates of the image are used as the center of the cursor image. 
#### Syntax

```
element/id/class{
    cursor: url(image_path.svg) x y default_keyword;
}
```

The x and y values work only if you are using custom cursor images. In the case of in-built cursor images, you are not required to provide any x and y values.

### Keywords in CSS
Keyword values are default values that define the type of cursor that you wish to use or any fallback cursor shape that you want to use if your specified cursor image fails to load.
If you wish to use a custom cursor shape, then you need to provide a fallback cursor keyword value. The value should be from the in-built cursor shapes. It is mandatory, as not all browsers support custom cursor shapes. So if your cursor shape fails to load, the browser will use the fallback value as the cursor shape for your element.

#### Syntax
```
element/id/class{
    cursor: url(image_path.svg) x y mandatory_default_value;
}
```

We have mentioned all the default keyword values below along with what all you can use them for.



| Keyword Value | Information they convey |
| -------- | -------- |
|auto     |The browser will determine cursor shape based on the element values. For example, if cursor is hovering over text, then cursor shape will be of text.|
|default | Cursor shape will be default shape, which would be an arrow.
|none| No Cursor will be rendered on the screen. Your screen will not have any cursor
|context-menu| A context value can be viewed by hovering over the element.
|help| You can get more information.
|pointer| A Link can be accessed by clicking on the element.
|progress| The web page is busy loading something in the background. The user can still access the loaded elements of the web page.
|wait| The web page is busy loading something in the background. The user needs to wait till the web page is fully loaded, to access the elements of the web page.
|cell| The user can access table cells.
|crosshair| The user can select from bitmap.
|text| The text inside the element can be selected horizontally.
|vertical-text|The text inside the element can be selected vertically.
|alias| A shortcut can be created.
|copy| You can copy something.
|move| You can move element or elements present inside.
|no-drop| The item you wish to drag and drop cannot be dropped at this current location.
|not-allowed| The requested action is blocked.
|grab| You can grab something. Usually used if you want to move something.
|grabbing| You have grabbed something, you can drag it and then drop it.
|all-scroll| You can scroll the element in any direction.
|col-resize| The item can be resized horizontally.
|row-resize| The item can be resized vertically.
|n-resize| The item can be increased in height from north side.
|e-resize| The width of item can be increased in height from east size.
|w-resize| The width of item can be increased in height from west size.
|s-resize| The item can be increased in height from south side.
|ne-resize| The item can be resized from north-east direction.
|nw-resize| The item can be resized from north-west direction.
|se-resize| The item can be resized from south-east direction.
|sw-resize| The item can be resized from south-west direction.
|ew-resize| The item can be resized from east-west direction.
|ns-resize| The item can be resized from north-south direction.
|nesw-resize| The item can be resized from all direction.
|nwse-resize| The item can be resized from all direction.
|zoom-in| The item can be zoomed into.
|zoom-out| The item can be zoomed out.

### Usage of Cursor in CSS
Why should you use the cursor property on your page? You might be thinking that. Well apart from the fact that it can make your cursor look pretty, there are other reasons why you should use the cursor property for your HTML Page. 
The main reason why you should use Cursor Property is because of UX. Believe it or not, the cursor property has more significance on UX rather than UI. Through various cursor shapes, you can easily convey your idea to the user. 
For example, let's say certain elements in your page are restricted to a user. What are the ways you can tell the user that they aren't allowed to access those areas? You can either put a heading above every element, or, you can use the cursor property. You can use set the cursor property to not-allowed in CSS, and this way if a user hovers over a particular element, which is not accessible to them, their cursor will change into a stop sign. This makes your page simple and lets you convey your element functionality to users more effectively.

#### Icon Size for Cursors in CSS
Icon sizes are restricted for the cursor in various browsers. The upper limit on the image size is fixed in different browsers. Certain browsers such as firefox have capped the upper limit of Icon size to be at 128*128 pixels. 
It is recommended that the image you are using as the cursor should have a size of 32*32 pixels. This image size will let you load your cursor image in most browsers. 

#### All Supported Image Formats
If you are using a custom image as a cursor shape, then you need to be careful about its format. Browsers support PNG and SVG v1.1 format for cursor images. If your image is in any other format, then the browser will not load it and fill use the mandatory keyword value provided by you instead. 
In case, you are using desktop browsers, you can use the .cur format for your cursor images. Desktop browsers support .cur format in addition to PNG and SVG format.

## Examples
Well, we have studied enough about cursors in CSS. It's time to gain knowledge from hands-on experience. 
For this, we would be creating a small project. We would be creating different elements or div in this project. Then for each element, we will provide them with a unique cursor shape and then see how each one of them works. We know that there are 37 different cursor shapes along with custom cursor shapes as well. So let's get started with it.

Our Design is simple. We would be building 38 individual div and for each div, we would be providing them with a unique cursor value. We have the design below, which we would be implementing.

![](My New Scaler URL)

First, we will build basic HTML, which is simple.
```
<!DOCTYPE html>
<html>
<body>
<h1>The Cursors of CSS</h1>
<div class="cursors">
    <div class="auto">auto</div>
    <div class="default">default</div>
    <div class="none">none</div>
    <div class="context-menu">context-menu</div>
    <div class="help">help</div>
    <div class="pointer">pointer</div>
    <div class="progress">progress</div>
    <div class="wait">wait</div>
    <div class="cell">cell</div>
    <div class="crosshair">crosshair</div>
    <div class="text">text</div>
    <div class="vertical-text">vertical-text</div>
    <div class="alias">alias</div>
    <div class="copy">copy</div>
    <div class="move">move</div>
    <div class="no-drop">no-drop</div>
    <div class="not-allowed">not-allowed</div>
    <div class="all-scroll">all-scroll</div>
    <div class="col-resize">col-resize</div>
    <div class="row-resize">row-resize</div>
    <div class="n-resize">n-resize</div>
    <div class="s-resize">s-resize</div>
    <div class="e-resize">e-resize</div>
    <div class="w-resize">w-resize</div>
    <div class="ns-resize">ns-resize</div>
    <div class="ew-resize">ew-resize</div>
    <div class="ne-resize">ne-resize</div>
    <div class="nw-resize">nw-resize</div>
    <div class="se-resize">se-resize</div>
    <div class="sw-resize">sw-resize</div>
    <div class="nesw-resize">nesw-resize</div>
    <div class="nwse-resize">nwse-resize</div>
</div>

</body>
</html>
```

Now, that we have covered HTML, let's make the above screen a little beautiful by using CSS.

```
body{
	text-align:center;
}

.cursors {
  display: flex;
  flex-wrap: wrap;
}
.cursors > div {
  flex: 150px;
  padding: 10px 2px;
  white-space: nowrap;
  border: 1px solid #eee;
  border-radius: 5px;
  margin: 0 5px 5px 0;
}
.cursors > div:hover {
  background: #eee;
}
```
Now our screen looks something like this.

![original-doc image](My New Scaler URL)

Now it's time to assign each div with its unique cursor shapes. As you can see in the HTML part, we have provided each nested div with a unique class Name. We would be using these unique class names to access each div and then render a unique cursor in each of this div.

The CSS would look something like this after we have implemented the above-given steps.

```
.auto            { cursor: auto; }
.default         { cursor: default; }
.none            { cursor: none; }
.context-menu    { cursor: context-menu; }
.help            { cursor: help; }
.pointer         { cursor: pointer; }
.progress        { cursor: progress; }
.wait            { cursor: wait; }
.cell            { cursor: cell; }
.crosshair       { cursor: crosshair; }
.text            { cursor: text; }
.vertical-text   { cursor: vertical-text; }
.alias           { cursor: alias; }
.copy            { cursor: copy; }
.move            { cursor: move; }
.no-drop         { cursor: no-drop; }
.not-allowed     { cursor: not-allowed; }
.all-scroll      { cursor: all-scroll; }
.col-resize      { cursor: col-resize; }
.row-resize      { cursor: row-resize; }
.n-resize        { cursor: n-resize; }
.e-resize        { cursor: e-resize; }
.s-resize        { cursor: s-resize; }
.w-resize        { cursor: w-resize; }
.ns-resize       { cursor: ns-resize; }
.ew-resize       { cursor: ew-resize; }
.ne-resize       { cursor: ne-resize; }
.nw-resize       { cursor: nw-resize; }
.se-resize       { cursor: se-resize; }
.sw-resize       { cursor: sw-resize; }
.nesw-resize     { cursor: nesw-resize; }
.nwse-resize     { cursor: nwse-resize; }

body{
	text-align:center;
}

.cursors {
  display: flex;
  flex-wrap: wrap;
}
.cursors > div {
  flex: 150px;
  padding: 10px 2px;
  white-space: nowrap;
  border: 1px solid #eee;
  border-radius: 5px;
  margin: 0 5px 5px 0;
}
.cursors > div:hover {
  background: #eee;
}
```

There you have it. Hover upon each div and you will get a unique cursor shape.

## Accessibility Concerns
Not every browser supports custom cursors. Around 80% of modern browsers allow users to use custom cursors. However, mobile browsers or mobile versions of modern browsers do not support custom cursor shapes. Therefore, you must be careful if you are dealing with custom cursor shapes. You should think about the user base and how a user might access any component of your website.

## Browser Support
The below browsers and their versions allow custom cursors. However, if you are dealing with any other browser, then you should check their documentation to make sure whether they support custom cursors or not.
* Google Chrome
* Mozilla Firefox
* Internet Explorer (IE)
* Microsoft Edge
* Opera
* Safari

The following mobile browsers support custom cursors.
* Android Chrome
* Android Browser

## Conclusion
* Cursors can be modified as per your convenience in CSS
* Custom cursors are important as they let the user know what they can do with certain elements in your website.
* You can either use in-built cursor shapes for your website, or you can even provide custom shapes for cursors on your website.
* You can change cursor shape by using the cursor keyword. It takes a value that defined your cursor shape.
* If you wish to use a custom shape for the cursor, then you should provide the path to your image inside url(). You should also provide a mandatory fallback value that which browser will use if it's unable to load the original cursor image.
* Not all browsers support custom cursors. You should look up and check if your browser allows a custom cursor or not.

## Related Properties
We have explained everything about cursors in CSS. If you wish to learn more about cursor or any other CSS property, then you can check the below-given links.
* [CSS Related Articles](https://www.scaler.com/topics/search/?tags=css)