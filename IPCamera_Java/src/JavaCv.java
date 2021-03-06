import com.googlecode.javacv.CanvasFrame;
import com.googlecode.javacv.OpenCVFrameGrabber;
import com.googlecode.javacv.cpp.opencv_core.IplImage;

/**
 *
 @Rakibuz Sultan Pranto
 * 
 */
public class JavaCv  {
    

public static void main(String[] args) throws Exception {
OpenCVFrameGrabber frameGrabber = new OpenCVFrameGrabber("http://192.168.0.2:8080/video?dummy=param.mjpg");
//OpenCVFrameGrabber frameGrabber = new OpenCVFrameGrabber("http://192.168.43.1:8080/video?dummy=param.jpeg");
    frameGrabber.setFormat("mjpeg");
   // frameGrabber.setFormat("jpeg");
    frameGrabber.start();
    IplImage iPimg = frameGrabber.grab();
    CanvasFrame canvasFrame = new CanvasFrame("Camera");
    canvasFrame.setCanvasSize(iPimg.width(), iPimg.height());
    
    while (canvasFrame.isVisible() && (iPimg = frameGrabber.grab()) != null) {
        canvasFrame.showImage(iPimg);
    }
    frameGrabber.stop();
    canvasFrame.dispose();
    System.exit(0);
}
}
