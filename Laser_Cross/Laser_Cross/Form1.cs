using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using AForge.Video.DirectShow;
using AForge.Video;
using AForge.Imaging.Filters;
using AForge.Imaging;
using AForge;
 


namespace Laser_Cross
{
    public partial class Form1 : Form
    {
        //calibration image
        Bitmap previous_image = null;

        //internal flag to see if calibration mode is enbaled
        bool _calibrate = false;


        //stores calibration data
        CalibrationData calibration_data = new CalibrationData();

        //to store video device
        VideoCaptureDevice VideoDevice = null;

        //internal flag to store if color tuning form is open
        bool _colortune = false;




        //Color filtering data(includes lower nad upper values of all three colors RGB)
        ColorData color_data = new ColorData();

        public Form1()
        {
            InitializeComponent();
        }

       
        private void VideoSource_Click(object sender, EventArgs e)
        {
            //creating instance of camerasource
            CameraSource camera_child = new CameraSource();

            camera_child.ShowDialog();

            //if OK was't clicked or no video device found  
            if (!camera_child.Click)
                return;

            //adding video source to this form
            VideoDevice = camera_child.VCD;

            //new frame event 
            VideoDevice.NewFrame += new AForge.Video.NewFrameEventHandler(VideoDevice_NewFrame);
            VideoDevice.Start();

            //enable filter editing, note by default filter is set to optimal values
            Filters.Enabled = true;

            //also enable tools
            Tools.Enabled = true;

        }

        private void VideoDevice_NewFrame(object sender, AForge.Video.NewFrameEventArgs eventArgs)
        {
            //making clone of frame recieved 
            Bitmap image = (Bitmap)eventArgs.Frame.Clone();
            //creating instance of color filtering for detectiong of laser light
            ColorFiltering colr_filter = new ColorFiltering();
            //setting the color filter properties
            colr_filter.Red = new AForge.IntRange(color_data.RedDown, color_data.RedUp);
            colr_filter.Blue = new AForge.IntRange(color_data.BlueDown, color_data.BlueUp);
            colr_filter.Green = new AForge.IntRange(color_data.GreenDown, color_data.GreenUp);



            //apply filter and storing filtered image in another bitmap
            Bitmap gray_image = colr_filter.Apply(image);

            //filter to convert RGB image to 8bpp gray scale for image processing 
            IFilter gray_filter = new GrayscaleBT709();
            gray_image = gray_filter.Apply(gray_image);



            //thrsholding a image
            Threshold th_filter = new Threshold(color_data.threshold);
            th_filter.ApplyInPlace(gray_image);

            if (color_data.erosion)
            {
                //erosion filter to filter out small unwanted pixels 
                Erosion3x3 err_filter = new Erosion3x3();
                err_filter.ApplyInPlace(gray_image);
            }

            if (color_data.dilation)
            {
                //dilation filter
                Dilatation3x3 dil_filter = new Dilatation3x3();
                dil_filter.ApplyInPlace(gray_image);
            }
            if (_colortune)
            {
                pictureBox1.Image = gray_image;
                return;
            }
            

            //initialize a blob counting object to count blobs in image
            BlobCounter bc = new BlobCounter();
            //arrange blobs by area
            bc.ObjectsOrder = ObjectsOrder.Area;
            bc.MinHeight = 15;
            bc.MaxWidth = 15;

            //process image for blobs
            bc.ProcessImage(gray_image);
            gray_image.Dispose();

            //get all the blobs from image
            Blob[] b = bc.GetObjectsInformation();

            //it should only one blob or no blob
            if (b.Length == 0 || b.Length > 1)
            {
                pictureBox1.Image = image;
           
                ycoord.Text = "Y coord: Not Valid";
                xcoord.Text = "X coord: Not Valid";
                return;
            }

            //finding center of gravity of blob detected
            AForge.IntPoint center_blob = (AForge.IntPoint)b[0].CenterOfGravity;



            //see if calibration is pressed
            if (_calibrate)
            {
                previous_image = (Bitmap)image.Clone();
                calibration_data.detected_point = new System.Drawing.Point(center_blob.X, center_blob.Y);
                return;
            }


            //finding y coordinate of blob from the bottom
            int _ycoord = Math.Abs(center_blob.Y - image.Height);
            ycoord.Text = "Y coord: " + Convert.ToString(_ycoord);
            

            int _xcoord = Math.Abs(center_blob.X - image.Width);
            xcoord.Text = "x coord: " + Convert.ToString(_xcoord);




            //NOTE: height of object from center of image is inversly propotional to range
            // to find constant of propotionality we need to calibrate according to some know values
            //so we need to stand at know range like 30 or 40 cm from camera and then press on calibrate
            if (calibration_data._calibrated)
            {
                double y_center = Math.Abs((float)(image.Height / 2) - center_blob.Y);
                double range = calibration_data.calibration_constant / y_center;

                RangeValue.Text = "Range: " + range.ToString("F2") + " cm";

            }

            //double x = pictureBox1.Size.Width / 2 + 256 * Math.Cos(100 * Math.PI / 180);
            //double y = pictureBox1.Size.Height / 2 + 256 * Math.Sin(100 * Math.PI / 180);
    

            //drawing rectangle on detected blob
            Graphics g = Graphics.FromImage(image);
            g.DrawRectangle(new Pen(Color.Blue), b[0].Rectangle);
           // g.DrawRectangle(new Pen(Color.Blue),pictureBox1.)
            g.DrawLine(
                new Pen(Color.Red),
                new System.Drawing.Point(center_blob.X, 0),
                new System.Drawing.Point(center_blob.X, center_blob.Y)
                );
            g.DrawLine(
               new Pen(Color.Red),
               new System.Drawing.Point(center_blob.X, pictureBox1.Size.Height),
               new System.Drawing.Point(center_blob.X, center_blob.Y)
               );

          
            g.DrawLine(
             new Pen(Color.Red),
             new System.Drawing.Point(center_blob.X, center_blob.Y),
             new System.Drawing.Point(pictureBox1.Width, center_blob.Y)
             
             );
            g.DrawLine(
            new Pen(Color.Red),
            new System.Drawing.Point(center_blob.X, center_blob.Y),
            new System.Drawing.Point(0, center_blob.Y)

            );
            g.Dispose();

            pictureBox1.Image = image;
             

        }

        private void CloseVideoSource()
        {
            if (!(VideoDevice == null))
                if (VideoDevice.IsRunning)
                {
                    VideoDevice.Stop();
                }
        }

        private void btn_ColorTune_Click(object sender, EventArgs e)
        {
            ColorTune child_tune = new ColorTune(ref color_data);

            _colortune = true;

            child_tune.ShowDialog();
            child_tune.Dispose();

            _colortune = false;
        }
    }
}
