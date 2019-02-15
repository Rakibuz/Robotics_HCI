using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using AForge.Video;
using System.Web;
using System.Net;
using System.IO.Ports;
namespace IPCamera
{
    public partial class Form1 : Form
    {
        MJPEGStream stream;
      

        public Form1()
        {
            InitializeComponent();
             stream = new MJPEGStream("http://192.168.0.2:8080/video");
           // stream = new MJPEGStream("http://192.168.0.105:8080/video");
            stream.NewFrame += stream_NewFrame;

        }

        private void stream_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            // throw new NotImplementedException();
            Bitmap bmp = (Bitmap)eventArgs.Frame.Clone();
            pictureBox1.Image = bmp;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            stream.Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            stream.Stop();
        }
    }
}
