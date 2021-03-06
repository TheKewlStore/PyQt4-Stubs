from typing import AnyStr
from typing import List
from typing import Union
from typing import Type

from PyQt4.QtCore import QObject
from PyQt4.QtCore import QSize
from PyQt4.QtCore import QString


class QtEnumeration(object):
    def __init__(self, value):
        self.value = value

    def __or__(self, other):
        return self.value | other.value


class QWidget(QObject):
    """ The QWidget class is the base class of all user interface objects.

        The widget is the atom of the user interface: it receives mouse, keyboard and other events from the window system, and paints a representation of
        itself on the screen. Every widget is rectangular, and they are sorted in a Z-order. A widget is clipped by its parent and by the widgets in front of it.

        A widget that is not embedded in a parent widget is called a window. Usually, windows have a frame and a title bar,
        although it is also possible to create windows without such decoration using suitable window flags).
        In Qt, QMainWindow and the various subclasses of QDialog are the most common window types.

        Every widget's constructor accepts one or two standard arguments:

        QWidget *parent = 0 is the parent of the new widget. If it is 0 (the default), the new widget will be a window.
        If not, it will be a child of parent, and be constrained by parent's geometry (unless you specify Qt::Window as window flag).
        Qt::WindowFlags f = 0 (where available) sets the window flags; the default is suitable for almost all widgets, but to get, for example,
        a window without a window system frame, you must use special flags.
        QWidget has many member functions, but some of them have little direct functionality; for example, QWidget has a font property, but never uses this itself.
        There are many subclasses which provide real functionality, such as QLabel, QPushButton, QListWidget, and QTabWidget.

        Top-Level and Child Widgets

        A widget without a parent widget is always an independent window (top-level widget). For these widgets, setWindowTitle() and setWindowIcon()
        set the title bar and icon respectively.

        Non-window widgets are child widgets, displayed within their parent widgets. Most widgets in Qt are mainly useful as child widgets.
        For example, it is possible to display a button as a top-level window, but most people prefer to put their buttons inside other widgets, such as QDialog.

        A parent widget containing various child widgets.

        The diagram above shows a QGroupBox widget being used to hold various child widgets in a layout provided by QGridLayout.
        The QLabel child widgets have been outlined to indicate their full sizes.

        If you want to use a QWidget to hold child widgets you will usually want to add a layout to the parent QWidget. See Layout Management for more information.

        Composite Widgets

        When a widget is used as a container to group a number of child widgets, it is known as a composite widget.
        These can be created by constructing a widget with the required visual properties - a QFrame,
        for example - and adding child widgets to it, usually managed by a layout. The above diagram shows such a composite widget that was created using Qt Designer.

        Composite widgets can also be created by subclassing a standard widget, such as QWidget or QFrame,
        and adding the necessary layout and child widgets in the constructor of the subclass. Many of the examples provided with Qt use this approach,
        and it is also covered in the Qt Tutorials.

        Custom Widgets and Painting

        Since QWidget is a subclass of QPaintDevice, subclasses can be used to display custom content that is composed using a series of
        painting operations with an instance of the QPainter class. This approach contrasts with the canvas-style approach used by the
        Graphics View Framework where items are added to a scene by the application and are rendered by the framework itself.

        Each widget performs all painting operations from within its paintEvent() function. This is called whenever the widget needs to be redrawn,
        either as a result of some external change or when requested by the application.

        The Analog Clock example shows how a simple widget can handle paint events.

        Size Hints and Size Policies

        When implementing a new widget, it is almost always useful to re-implement sizeHint() to provide a reasonable default size for the widget and to set
        the correct size policy with setSizePolicy().

        By default, composite widgets which do not provide a size hint will be sized according to the space requirements of their child widgets.

        The size policy lets you supply good default behavior for the layout management system, so that other widgets can contain and manage yours easily.
        The default size policy indicates that the size hint represents the preferred size of the widget, and this is often good enough for many widgets.

        Note: The size of top-level widgets are constrained to 2/3 of the desktop's height and width. You can resize() the widget manually if these bounds are inadequate.

        Events

        Widgets respond to events that are typically caused by user actions. Qt delivers events to widgets by calling specific event handler functions with instances of
        QEvent subclasses containing information about each event.

        If your widget only contains child widgets, you probably do not need to implement any event handlers. If you want to detect a mouse click in a child widget call
        the child's underMouse() function inside the widget's mousePressEvent().

        The Scribble example implements a wider set of events to handle mouse movement, button presses, and window resizing.

        You will need to supply the behavior and content for your own widgets, but here is a brief overview of the events that are relevant to QWidget,
        starting with the most common ones:

        paintEvent() is called whenever the widget needs to be repainted. Every widget displaying custom content must implement it.
        Painting using a QPainter can only take place in a paintEvent() or a function called by a paintEvent().
        resizeEvent() is called when the widget has been resized.
        mousePressEvent() is called when a mouse button is pressed while the mouse cursor is inside the widget, or when the widget has
        grabbed the mouse using grabMouse(). Pressing the mouse without releasing it is effectively the same as calling grabMouse().
        mouseReleaseEvent() is called when a mouse button is released. A widget receives mouse release events when it has received the corresponding mouse press event.
        This means that if the user presses the mouse inside your widget, then drags the mouse somewhere else before releasing the mouse button,
        your widget receives the release event. There is one exception: if a popup menu appears while the mouse button is held down,
        this popup immediately steals the mouse events.
        mouseDoubleClickEvent() is called when the user double-clicks in the widget. If the user double-clicks,
        the widget receives a mouse press event, a mouse release event and finally this event instead of a second mouse press event.
        (Some mouse move events may also be received if the mouse is not held steady during this operation.)
        It is not possible to distinguish a click from a double-click until the second click arrives.
        (This is one reason why most GUI books recommend that double-clicks be an extension of single-clicks, rather than trigger a different action.)
        Widgets that accept keyboard input need to re-implement a few more event handlers:

        keyPressEvent() is called whenever a key is pressed, and again when a key has been held down long enough for it to auto-repeat.
        The Tab and Shift+Tab keys are only passed to the widget if they are not used by the focus-change mechanisms.
        To force those keys to be processed by your widget, you must re-implement QWidget::event().
        focusInEvent() is called when the widget gains keyboard focus (assuming you have called setFocusPolicy()).
        Well-behaved widgets indicate that they own the keyboard focus in a clear but discreet way.
        focusOutEvent() is called when the widget loses keyboard focus.
        You may be required to also re-implement some of the less common event handlers:

        mouseMoveEvent() is called whenever the mouse moves while a mouse button is held down. This can be useful during drag and drop operations.
        If you call setMouseTracking(true), you get mouse move events even when no buttons are held down. (See also the Drag and Drop guide.)
        keyReleaseEvent() is called whenever a key is released and while it is held down (if the key is auto-repeating).
        In that case, the widget will receive a pair of key release and key press event for every repeat.
        The Tab and Shift+Tab keys are only passed to the widget if they are not used by the focus-change mechanisms.
        To force those keys to be processed by your widget, you must reimplement QWidget::event().
        wheelEvent() is called whenever the user turns the mouse wheel while the widget has the focus.
        enterEvent() is called when the mouse enters the widget's screen space. (This excludes screen space owned by any of the widget's children.)
        leaveEvent() is called when the mouse leaves the widget's screen space. If the mouse enters a child widget it will not cause a leaveEvent().
        moveEvent() is called when the widget has been moved relative to its parent.
        closeEvent() is called when the user closes the widget (or when close() is called).
        There are also some rather obscure events described in the documentation for QEvent::Type. To handle these events, you need to reimplement event() directly.

        The default implementation of event() handles Tab and Shift+Tab (to move the keyboard focus), and passes on most of the other events
        to one of the more specialized handlers above.

        Events and the mechanism used to deliver them are covered in The Event System.

        Groups of Functions and Properties

        Context	Functions and Properties
        Window functions	show(), hide(), raise(), lower(), close().
        Top-level windows	windowModified, windowTitle, windowIcon, windowIconText, isActiveWindow, activateWindow(), minimized, showMinimized(), maximized,
        showMaximized(), fullScreen, showFullScreen(), showNormal().
        Window contents	update(), repaint(), scroll().
        Geometry	pos, x(), y(), rect, size, width(), height(), move(), resize(), sizePolicy, sizeHint(), minimumSizeHint(), updateGeometry(), layout(), frameGeometry,
        geometry, childrenRect, childrenRegion, adjustSize(), mapFromGlobal(), mapToGlobal(), mapFromParent(), mapToParent(), maximumSize, minimumSize, sizeIncrement,
        baseSize, setFixedSize()
        Mode	visible, isVisibleTo(), enabled, isEnabledTo(), modal, isWindow(), mouseTracking, updatesEnabled, visibleRegion().
        Look and feel	style(), setStyle(), styleSheet, cursor, font, palette, backgroundRole(), setBackgroundRole(), fontInfo(), fontMetrics().
        Keyboard focus functions	focus, focusPolicy, setFocus(), clearFocus(), setTabOrder(), setFocusProxy(), focusNextChild(), focusPreviousChild().
        Mouse and keyboard grabbing	grabMouse(), releaseMouse(), grabKeyboard(), releaseKeyboard(), mouseGrabber(), keyboardGrabber().
        Event handlers	event(), mousePressEvent(), mouseReleaseEvent(), mouseDoubleClickEvent(), mouseMoveEvent(), keyPressEvent(), keyReleaseEvent(), focusInEvent(),
         focusOutEvent(), wheelEvent(), enterEvent(), leaveEvent(), paintEvent(), moveEvent(), resizeEvent(), closeEvent(), dragEnterEvent(), dragMoveEvent(),
         dragLeaveEvent(), dropEvent(), childEvent(), showEvent(), hideEvent(), customEvent(). changeEvent(),
        System functions	parentWidget(), window(), setParent(), winId(), find(), metric().
        Interactive help	setToolTip(), setWhatsThis()
        Widget Style Sheets

        In addition to the standard widget styles for each platform, widgets can also be styled according to rules specified in a style sheet.
        This feature enables you to customize the appearance of specific widgets to provide visual cues to users about their purpose.
        For example, a button could be styled in a particular way to indicate that it performs a destructive action.

        The use of widget style sheets is described in more detail in the Qt Style Sheets document.

        Transparency and Double Buffering

        Since Qt 4.0, QWidget automatically double-buffers its painting, so there is no need to write double-buffering code in paintEvent() to avoid flicker.

        Since Qt 4.1, the Qt::WA_ContentsPropagated widget attribute has been deprecated. Instead, the contents of parent widgets are propagated by default to
         each of their children as long as Qt::WA_PaintOnScreen is not set. Custom widgets can be written to take advantage of this feature by updating irregular
         regions (to create non-rectangular child widgets), or painting with colors that have less than full alpha component. The following diagram shows how
         attributes and properties of a custom widget can be fine-tuned to achieve different effects.



        In the above diagram, a semi-transparent rectangular child widget with an area removed is constructed and added to a parent widget (a QLabel showing a pixmap).
         Then, different properties and widget attributes are set to achieve different effects:

        The left widget has no additional properties or widget attributes set. This default state suits most custom widgets using transparency, are irregularly-shaped,
         or do not paint over their entire area with an opaque brush.
        The center widget has the autoFillBackground property set. This property is used with custom widgets that rely on the widget to supply a default background,
         and do not paint over their entire area with an opaque brush.
        The right widget has the Qt::WA_OpaquePaintEvent widget attribute set. This indicates that the widget will paint over its entire area with opaque colors. T
        he widget's area will initially be uninitialized, represented in the diagram with a red diagonal grid pattern that shines through the overpainted area.
        The Qt::WA_OpaquePaintArea attribute is useful for widgets that need to paint their own specialized contents quickly and do not need a default filled background.
        To rapidly update custom widgets with simple background colors, such as real-time plotting or graphing widgets, it is better to define a suitable
         background color (using setBackgroundRole() with the QPalette::Window role), set the autoFillBackground property, and only implement the necessary
         drawing functionality in the widget's paintEvent().

        To rapidly update custom widgets that constantly paint over their entire areas with opaque content, e.g., video streaming widgets,
        it is better to set the widget's Qt::WA_OpaquePaintEvent, avoiding any unnecessary overhead associated with repainting the widget's background.

        If a widget has both the Qt::WA_OpaquePaintEvent widget attribute and the autoFillBackground property set, the Qt::WA_OpaquePaintEvent attribute takes precedence.
         Depending on your requirements, you should choose either one of them.

        Since Qt 4.1, the contents of parent widgets are also propagated to standard Qt widgets. This can lead to some unexpected results if the parent widget
        is decorated in a non-standard way, as shown in the diagram below.



        The scope for customizing the painting behavior of standard Qt widgets, without resorting to subclassing, is slightly less than that possible for custom widgets.
         Usually, the desired appearance of a standard widget can be achieved by setting its autoFillBackground property.

        Creating Translucent Windows

        Since Qt 4.5, it has been possible to create windows with translucent regions on window systems that support compositing.

        To enable this feature in a top-level widget, set its Qt::WA_TranslucentBackground attribute with setAttribute() and ensure that its background is painted with
        non-opaque colors in the regions you want to be partially transparent.

        Platform notes:

        X11: This feature relies on the use of an X server that supports ARGB visuals and a compositing window manager.
        Windows: The widget needs to have the Qt::FramelessWindowHint window flag set for the translucency to work.
        Native Widgets vs Alien Widgets

        Introduced in Qt 4.4, alien widgets are widgets unknown to the windowing system. They do not have a native window handle associated with them.
        This feature significantly speeds up widget painting, resizing, and removes flicker.

        Should you require the old behavior with native windows, you can choose one of the following options:

        Use the QT_USE_NATIVE_WINDOWS=1 in your environment.
        Set the Qt::AA_NativeWindows attribute on your application. All widgets will be native widgets.
        Set the Qt::WA_NativeWindow attribute on widgets: The widget itself and all of its ancestors will become native (unless Qt::WA_DontCreateNativeAncestors is set).
        Call QWidget::winId to enforce a native window (this implies 3).
        Set the Qt::WA_PaintOnScreen attribute to enforce a native window (this implies 3).
        Softkeys

        Since Qt 4.6, Softkeys are usually physical keys on a device that have a corresponding label or other visual representation on the screen that is generally
        located next to its physical counterpart. They are most often found on mobile phone platforms. In modern touch based user interfaces it is also possible to
        have softkeys that do not correspond to any physical keys. Softkeys differ from other onscreen labels in that they are contextual.

        In Qt, contextual softkeys are added to a widget by calling addAction() and passing a QAction with a softkey role set on it. When the widget containing the
        softkey actions has focus, its softkeys should appear in the user interface. Softkeys are discovered by traversing the widget hierarchy so it is possible
        to define a single set of softkeys that are present at all times by calling addAction() for a given top level widget.

        On some platforms, this concept overlaps with QMenuBar such that if no other softkeys are found and the top level widget is a QMainWindow containing a QMenuBar,
         the menu-bar actions may appear on one of the softkeys.

        Note: Currently softkeys are only supported on the Symbian Platform.
    """
    class RenderFlag(QtEnumeration):
        """ This enum describes how to render the widget when calling QWidget::render().
        """
        ...

    DrawWindowBackground = RenderFlag(0x1)
    """ If you enable this option, the widget's background is rendered into the target even if autoFillBackground is not set. By default, this option is enabled."""
    DrawChildren = RenderFlag(0x2)
    """ If you enable this option, the widget's children are rendered recursively into the target. By default, this option is enabled."""
    IgnoreMask = RenderFlag(0x4)
    """ If you enable this option, the widget's QWidget::mask() is ignored when rendering into the target. By default, this option is disabled."""

    def acceptDrops(self) -> bool:
        """ This property holds whether drop events are enabled for this widget.

            Setting this property to true announces to the system that this widget may be able to accept drop events.

            If the widget is the desktop (windowType() == Qt::Desktop), this may fail if another application is using the desktop; you can call acceptDrops()
            to test if this occurs.

            Warning: Do not modify this property in a drag and drop event handler.

            By default, this property is false.

            :return: True if this widget accepts drops, false otherwise.
        """
        ...

    def setAcceptDrops(self, on: bool):
        """ Set the acceptDrops property.

            See QWidget.acceptDrops
        """
        ...

    def accessibleDescription(self) -> Union[AnyStr, QString]:
        """ This property holds the widget's description as seen by assistive technologies.

            By default, this property contains an empty string.

            :return: The value of the accessibleDescription property.
        """
        ...

    def setAccessibleDescription(self, description: Union[AnyStr, QString]):
        """ Set the accessibleDescription property.

            See QWidget.accessibleDescription

            :param description: The new description.
        """

    def accessibleName(self) -> Union[AnyStr, QString]:
        """ This property holds the widget's name as seen by assistive technologies.

            This property is used by accessible clients to identify, find, or announce the widget for accessible clients.

            By default, this property contains an empty string.

            :return: The value of the accessibleName property.
        """
        ...

    def setAccessibleName(self, name: Union[AnyStr, QString]):
        """ Set the accessibleName property.

            See QWidget.accessibleName

            :param name: The new name.
        """
        ...

    def autoFillBackground(self) -> bool:
        """ This property holds whether the widget background is filled automatically.

            If enabled, this property will cause Qt to fill the background of the widget before invoking the paint event.
            The color used is defined by the QPalette::Window color role from the widget's palette.

            In addition, Windows are always filled with QPalette::Window, unless the WA_OpaquePaintEvent or WA_NoSystemBackground attributes are set.

            This property cannot be turned off (i.e., set to false) if a widget's parent has a static gradient for its background.

            Warning: Use this property with caution in conjunction with Qt Style Sheets. When a widget has a style sheet with a valid background or a border-image,
            this property is automatically disabled.

            By default, this property is false.

            This property was introduced in Qt 4.1.

            :return: True if autoFillBackground is enabled, otherwise False.
        """
        ...

    def setAutoFillBackground(self, enabled: bool):
        """ Set the autoFillBackground property.

            :param enabled: Whether or not auto fill background should be enabled.
        """
        ...

    def baseSize(self) -> QSize:
        """ This property holds the base size of the widget.

            The base size is used to calculate a proper widget size if the widget defines sizeIncrement().

            By default, for a newly-created widget, this property contains a size with zero width and height.

            :return:
        """
        ...