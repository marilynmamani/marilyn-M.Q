package pe.edu.upeu.gui;

import javax.swing.JFrame;
import pe.edu.upeu.util.UtilsX;
import java.awt.event.*;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
public class MainGUI extends JFrame implements ActionListener{

    private static final long serialVersionUID = 1L;
    int numeros;
    JPanel panel;
    JTextField texto;
    JScrollPane scrollPane=new JScrollPane();
    BufferedImage image;
    JTable table;
    JMenuBar mb;
    JMenu m1;
    JMenu m2;
    JMenuItem m11;
    JMenuItem m22;
    UtilsX obj=new UtilsX();
    JPanel panelFoot;
    JButton send, reset;

    public MainGUI() {
        this.setTitle("SystemMain@DMP");  
        
        this.setVisible(true);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // TODO Auto-generated method stub
        
    }

}
