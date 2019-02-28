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

namespace Laser_Cross
{
    public partial class CameraSource : Form
    {

        //flag to check if ok was clicked and videosource is present
        private bool _click = false;

        //selected video source is stored here
        public VideoCaptureDevice VCD = null;

        //collection storing all video capture devices available
        FilterInfoCollection FIC = new FilterInfoCollection(FilterCategory.VideoInputDevice);
        //Property
        public bool Click
        {
            get { return _click; }
        }
        public CameraSource()
        {
            InitializeComponent();
            //if no video device is found then disable OK button
            if (FIC.Count == 0)
            {
               comboBox1.Items.Add("No Device Found");
                btn_ok.Enabled = false;
                comboBox1.Enabled = false;
            }
            else
            {
                //adding all video devices in combo box for selection
                foreach (FilterInfo VideoDevice in FIC)
                {
                   comboBox1.Items.Add(VideoDevice.Name);
                }
            }

            //default selection index
              comboBox1.SelectedIndex = 0;
        }

        private void btn_ok_Click(object sender, EventArgs e)
        {
            _click = true;

            //Storing the video device selected by user
            VCD = new VideoCaptureDevice(FIC[comboBox1.SelectedIndex].MonikerString);

            this.Close();
        }

        private void btn_clc_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
