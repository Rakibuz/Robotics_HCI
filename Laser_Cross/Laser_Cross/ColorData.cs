using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Laser_Cross
{
    public class ColorData
    {

        public bool dilation = true;
        public bool erosion = true;

        public int threshold = 40;

        public int RedUp = 255;
        public int RedDown = 0;

        public int BlueUp = 255;
        public int BlueDown = 0;

        public int GreenUp = 255;
        public int GreenDown = 0;

        //default constructor
        public ColorData() { }

        //constructor
        public ColorData(int RedUp, int RedDown, int BlueUp, int BlueDown, int GreenUp, int GreenDown, int threshold, bool dilation, bool erosion)
        {
            this.dilation = dilation;
            this.erosion = erosion;
            this.threshold = threshold;
            this.RedUp = RedUp;
            this.RedDown = RedDown;
            this.BlueDown = BlueDown;
            this.GreenDown = GreenDown;
            this.GreenUp = GreenUp;
            this.BlueUp = BlueUp;
        }
    
}
}
