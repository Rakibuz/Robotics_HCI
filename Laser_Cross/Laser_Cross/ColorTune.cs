using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using AForge.Controls;

namespace Laser_Cross
{
    public partial class ColorTune : Form
    {
        ColorData cd;

        public ColorTune(ref ColorData color_data)
        {
            InitializeComponent();

            //refrence of color data
            cd = color_data;

            //setting the min and max values of each slider
            MinRed.Value = color_data.RedDown;
            MaxRed.Value = color_data.RedUp;

            MinBlue.Value = color_data.BlueDown;
            MaxBlue.Value = color_data.BlueUp;

            MinGreen.Value = color_data.GreenDown;
            MaxGreen.Value = color_data.GreenUp;

            //setting threshold value
            Threshold.Value = color_data.threshold;

            //checkboxes
            Dilation.Checked = color_data.dilation;
            Erosion.Checked = color_data.erosion;

        }

        private void minRed_ValueChanged(object sender, EventArgs e)
        {
            cd.RedDown = Convert.ToInt32(MinRed.Value);
        }

        private void maxRed_ValueChanged(object sender, EventArgs e)
        {
            cd.RedUp = Convert.ToInt32(MaxRed.Value);
        }

        private void minGreen_ValueChanged(object sender, EventArgs e)
        {
            cd.GreenDown = Convert.ToInt32(MinGreen.Value);

        }

        private void maxGreen_ValueChanged(object sender, EventArgs e)
        {
            cd.GreenDown = Convert.ToInt32(MinGreen.Value);
        }

        private void minBlue_ValueChanged(object sender, EventArgs e)
        {
            cd.BlueDown = Convert.ToInt32(MinBlue.Value);
        }
        private void maxBlue_ValueChanged(object sender, EventArgs e)
        {
            cd.BlueUp = Convert.ToInt32(MaxBlue.Value);
        }
    }
}
