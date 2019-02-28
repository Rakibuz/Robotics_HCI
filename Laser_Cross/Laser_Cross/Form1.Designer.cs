namespace Laser_Cross
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.toolStrip1 = new System.Windows.Forms.ToolStrip();
            this.toolStripDropDownButton1 = new System.Windows.Forms.ToolStripDropDownButton();
            this.VideoSource = new System.Windows.Forms.ToolStripMenuItem();
            this.Filters = new System.Windows.Forms.ToolStripDropDownButton();
            this.btn_ColorTune = new System.Windows.Forms.ToolStripMenuItem();
            this.Tools = new System.Windows.Forms.ToolStripDropDownButton();
            this.calibrateToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.StatusStrip = new System.Windows.Forms.StatusStrip();
            this.RangeValue = new System.Windows.Forms.ToolStripStatusLabel();
            this.Blank = new System.Windows.Forms.ToolStripStatusLabel();
            this.ycoord = new System.Windows.Forms.ToolStripStatusLabel();
            this.xcoord = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.StatusStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // toolStrip1
            // 
            this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripDropDownButton1,
            this.Filters,
            this.Tools});
            this.toolStrip1.Location = new System.Drawing.Point(0, 0);
            this.toolStrip1.Name = "toolStrip1";
            this.toolStrip1.Size = new System.Drawing.Size(406, 25);
            this.toolStrip1.TabIndex = 0;
            this.toolStrip1.Text = "toolStrip1";
            // 
            // toolStripDropDownButton1
            // 
            this.toolStripDropDownButton1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.toolStripDropDownButton1.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.VideoSource});
            this.toolStripDropDownButton1.Image = ((System.Drawing.Image)(resources.GetObject("toolStripDropDownButton1.Image")));
            this.toolStripDropDownButton1.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripDropDownButton1.Name = "toolStripDropDownButton1";
            this.toolStripDropDownButton1.Size = new System.Drawing.Size(42, 22);
            this.toolStripDropDownButton1.Text = "Add";
            // 
            // VideoSource
            // 
            this.VideoSource.Name = "VideoSource";
            this.VideoSource.Size = new System.Drawing.Size(140, 22);
            this.VideoSource.Text = "VideoSource";
            this.VideoSource.Click += new System.EventHandler(this.VideoSource_Click);
            // 
            // Filters
            // 
            this.Filters.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.Filters.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.btn_ColorTune});
            this.Filters.Image = ((System.Drawing.Image)(resources.GetObject("Filters.Image")));
            this.Filters.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.Filters.Name = "Filters";
            this.Filters.Size = new System.Drawing.Size(51, 22);
            this.Filters.Text = "Filters";
            // 
            // btn_ColorTune
            // 
            this.btn_ColorTune.Name = "btn_ColorTune";
            this.btn_ColorTune.Size = new System.Drawing.Size(133, 22);
            this.btn_ColorTune.Text = "Color Tune";
            this.btn_ColorTune.Click += new System.EventHandler(this.btn_ColorTune_Click);
            // 
            // Tools
            // 
            this.Tools.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.Tools.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.calibrateToolStripMenuItem});
            this.Tools.Image = ((System.Drawing.Image)(resources.GetObject("Tools.Image")));
            this.Tools.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.Tools.Name = "Tools";
            this.Tools.Size = new System.Drawing.Size(51, 22);
            this.Tools.Text = " Tools";
            // 
            // calibrateToolStripMenuItem
            // 
            this.calibrateToolStripMenuItem.Name = "calibrateToolStripMenuItem";
            this.calibrateToolStripMenuItem.Size = new System.Drawing.Size(121, 22);
            this.calibrateToolStripMenuItem.Text = "Calibrate";
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(12, 28);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(388, 335);
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            // 
            // StatusStrip
            // 
            this.StatusStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.RangeValue,
            this.Blank,
            this.ycoord,
            this.xcoord});
            this.StatusStrip.Location = new System.Drawing.Point(0, 388);
            this.StatusStrip.Name = "StatusStrip";
            this.StatusStrip.Size = new System.Drawing.Size(406, 22);
            this.StatusStrip.TabIndex = 6;
            this.StatusStrip.Text = "statusStrip1";
            // 
            // RangeValue
            // 
            this.RangeValue.Font = new System.Drawing.Font("Tahoma", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.RangeValue.ForeColor = System.Drawing.SystemColors.ControlDarkDark;
            this.RangeValue.Name = "RangeValue";
            this.RangeValue.Size = new System.Drawing.Size(112, 17);
            this.RangeValue.Text = "Range: Not calibrated";
            // 
            // Blank
            // 
            this.Blank.ForeColor = System.Drawing.SystemColors.AppWorkspace;
            this.Blank.Name = "Blank";
            this.Blank.Size = new System.Drawing.Size(16, 17);
            this.Blank.Text = ":::";
            // 
            // ycoord
            // 
            this.ycoord.ForeColor = System.Drawing.SystemColors.ControlDarkDark;
            this.ycoord.Name = "ycoord";
            this.ycoord.Size = new System.Drawing.Size(102, 17);
            this.ycoord.Text = "Y coord: Not valid";
            // 
            // xcoord
            // 
            this.xcoord.Name = "xcoord";
            this.xcoord.Size = new System.Drawing.Size(102, 17);
            this.xcoord.Text = "X coord: Not valid";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(406, 410);
            this.Controls.Add(this.StatusStrip);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.toolStrip1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "Form1";
            this.Text = "Form1";
            this.toolStrip1.ResumeLayout(false);
            this.toolStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.StatusStrip.ResumeLayout(false);
            this.StatusStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ToolStrip toolStrip1;
        private System.Windows.Forms.ToolStripDropDownButton toolStripDropDownButton1;
        private System.Windows.Forms.ToolStripMenuItem VideoSource;
        private System.Windows.Forms.ToolStripDropDownButton Filters;
        private System.Windows.Forms.ToolStripMenuItem btn_ColorTune;
        private System.Windows.Forms.ToolStripDropDownButton Tools;
        private System.Windows.Forms.ToolStripMenuItem calibrateToolStripMenuItem;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.StatusStrip StatusStrip;
        private System.Windows.Forms.ToolStripStatusLabel RangeValue;
        private System.Windows.Forms.ToolStripStatusLabel Blank;
        private System.Windows.Forms.ToolStripStatusLabel ycoord;
        private System.Windows.Forms.ToolStripStatusLabel xcoord;
    }
}

