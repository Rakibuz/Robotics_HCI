namespace Laser_Cross
{
    partial class ColorTune
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.MaxBlue = new System.Windows.Forms.NumericUpDown();
            this.MinBlue = new System.Windows.Forms.NumericUpDown();
            this.MaxGreen = new System.Windows.Forms.NumericUpDown();
            this.MinGreen = new System.Windows.Forms.NumericUpDown();
            this.MaxRed = new System.Windows.Forms.NumericUpDown();
            this.MinRed = new System.Windows.Forms.NumericUpDown();
            this.Erosion = new System.Windows.Forms.CheckBox();
            this.label6 = new System.Windows.Forms.Label();
            this.Dilation = new System.Windows.Forms.CheckBox();
            this.label5 = new System.Windows.Forms.Label();
            this.Threshold = new System.Windows.Forms.TrackBar();
            this.label2 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.MaxBlue)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.MinBlue)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.MaxGreen)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.MinGreen)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.MaxRed)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.MinRed)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.Threshold)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.MaxBlue);
            this.groupBox1.Controls.Add(this.MinBlue);
            this.groupBox1.Controls.Add(this.MaxGreen);
            this.groupBox1.Controls.Add(this.MinGreen);
            this.groupBox1.Controls.Add(this.MaxRed);
            this.groupBox1.Controls.Add(this.MinRed);
            this.groupBox1.Controls.Add(this.Erosion);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.Dilation);
            this.groupBox1.Controls.Add(this.label5);
            this.groupBox1.Controls.Add(this.Threshold);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.label4);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(35, 50);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(372, 169);
            this.groupBox1.TabIndex = 23;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Tuning";
            // 
            // MaxBlue
            // 
            this.MaxBlue.Location = new System.Drawing.Point(225, 77);
            this.MaxBlue.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.MaxBlue.Name = "MaxBlue";
            this.MaxBlue.Size = new System.Drawing.Size(120, 20);
            this.MaxBlue.TabIndex = 28;
            // 
            // MinBlue
            // 
            this.MinBlue.Location = new System.Drawing.Point(96, 77);
            this.MinBlue.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.MinBlue.Name = "MinBlue";
            this.MinBlue.Size = new System.Drawing.Size(120, 20);
            this.MinBlue.TabIndex = 27;
            this.MinBlue.ValueChanged += new System.EventHandler(this.minBlue_ValueChanged);
            // 
            // MaxGreen
            // 
            this.MaxGreen.Location = new System.Drawing.Point(225, 51);
            this.MaxGreen.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.MaxGreen.Name = "MaxGreen";
            this.MaxGreen.Size = new System.Drawing.Size(120, 20);
            this.MaxGreen.TabIndex = 26;
            this.MaxGreen.ValueChanged += new System.EventHandler(this.maxGreen_ValueChanged);
            // 
            // MinGreen
            // 
            this.MinGreen.Location = new System.Drawing.Point(96, 51);
            this.MinGreen.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.MinGreen.Name = "MinGreen";
            this.MinGreen.Size = new System.Drawing.Size(120, 20);
            this.MinGreen.TabIndex = 25;
            this.MinGreen.ValueChanged += new System.EventHandler(this.minGreen_ValueChanged);
            // 
            // MaxRed
            // 
            this.MaxRed.Location = new System.Drawing.Point(225, 25);
            this.MaxRed.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.MaxRed.Name = "MaxRed";
            this.MaxRed.Size = new System.Drawing.Size(120, 20);
            this.MaxRed.TabIndex = 24;
            this.MaxRed.ValueChanged += new System.EventHandler(this.maxRed_ValueChanged);
            // 
            // MinRed
            // 
            this.MinRed.Location = new System.Drawing.Point(96, 25);
            this.MinRed.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.MinRed.Name = "MinRed";
            this.MinRed.Size = new System.Drawing.Size(120, 20);
            this.MinRed.TabIndex = 23;
            this.MinRed.ValueChanged += new System.EventHandler(this.minRed_ValueChanged);
            // 
            // Erosion
            // 
            this.Erosion.AutoSize = true;
            this.Erosion.Location = new System.Drawing.Point(192, 141);
            this.Erosion.Name = "Erosion";
            this.Erosion.Size = new System.Drawing.Size(15, 14);
            this.Erosion.TabIndex = 22;
            this.Erosion.UseVisualStyleBackColor = true;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(116, 141);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(70, 13);
            this.label6.TabIndex = 21;
            this.label6.Text = "Erosion Filter:";
            // 
            // Dilation
            // 
            this.Dilation.AutoSize = true;
            this.Dilation.Location = new System.Drawing.Point(82, 141);
            this.Dilation.Name = "Dilation";
            this.Dilation.Size = new System.Drawing.Size(15, 14);
            this.Dilation.TabIndex = 20;
            this.Dilation.UseVisualStyleBackColor = true;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(6, 141);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(70, 13);
            this.label5.TabIndex = 19;
            this.label5.Text = "Dilation Filter:";
            // 
            // Threshold
            // 
            this.Threshold.AutoSize = false;
            this.Threshold.Location = new System.Drawing.Point(75, 102);
            this.Threshold.Maximum = 255;
            this.Threshold.Minimum = 1;
            this.Threshold.Name = "Threshold";
            this.Threshold.Size = new System.Drawing.Size(270, 17);
            this.Threshold.TabIndex = 18;
            this.Threshold.Value = 40;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 49);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(69, 13);
            this.label2.TabIndex = 9;
            this.label2.Text = "Green range:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(6, 106);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(57, 13);
            this.label4.TabIndex = 17;
            this.label4.Text = "Threshold:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 74);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(61, 13);
            this.label3.TabIndex = 10;
            this.label3.Text = "Blue range:";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 25);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(60, 13);
            this.label1.TabIndex = 8;
            this.label1.Text = "Red range:";
            // 
            // ColorTune
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(441, 302);
            this.Controls.Add(this.groupBox1);
            this.Name = "ColorTune";
            this.Text = "ColorTune";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.MaxBlue)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.MinBlue)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.MaxGreen)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.MinGreen)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.MaxRed)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.MinRed)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.Threshold)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.NumericUpDown MaxBlue;
        private System.Windows.Forms.NumericUpDown MinBlue;
        private System.Windows.Forms.NumericUpDown MaxGreen;
        private System.Windows.Forms.NumericUpDown MinGreen;
        private System.Windows.Forms.NumericUpDown MaxRed;
        private System.Windows.Forms.NumericUpDown MinRed;
        private System.Windows.Forms.CheckBox Erosion;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.CheckBox Dilation;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TrackBar Threshold;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label1;
    }
}