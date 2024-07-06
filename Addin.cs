using Autodesk.Revit.UI;
using System.IO;
using System.Reflection;
using System.Windows.Media.Imaging;
using System.Windows.Media;

namespace BimScript
{
    public class Addin : IExternalApplication
    {
        private readonly string _AssemblyLocation = Assembly.GetExecutingAssembly().Location;
        private readonly string _AssemblyName = "BimScript";

        public Result OnStartup (UIControlledApplication application)
        {
            CreateRibbon(application);
            return Result.Succeeded;
        }

        public Result OnShutdown(UIControlledApplication application)
        {
            return Result.Succeeded;
        }

        private void CreateRibbon(UIControlledApplication application)
        {
            var panel = GetAddinPanel(application, "Script Gateway");

            panel.AddItem(CreatePushButtonData(
                "ConfigurationCmd",
                "Configuration",
                "Open the configuration settings",
                "Open the configuration settings",
                Properties.Resources.python_logo));

            panel.AddItem(CreatePushButtonData(
                "ScriptCmd",
                "Command",
                "Launch a Python script",
                "Launch a Python script",
                Properties.Resources.python_logo));
        }

        private PushButtonData CreatePushButtonData(string className, string publicName, string toolTip, string description, byte[] byteArray)
        {
            var full_class_name = string.Join(".", _AssemblyName, className);
            var data = new PushButtonData(className, publicName, _AssemblyLocation, full_class_name)
            {
                ToolTip = toolTip,
                LongDescription = description,
                Image = ByteArrayToImageSource(byteArray, 64),
                LargeImage = ByteArrayToImageSource(byteArray, 64)
            };
            return data;
        }

        private static RibbonPanel GetAddinPanel(UIControlledApplication application, string panelName)
        {
            var panels = application.GetRibbonPanels(Tab.AddIns);
            foreach (var panel in panels)
            {
                if (panel.Name == panelName)
                {
                    return panel;
                }
            }
            return application.CreateRibbonPanel(Tab.AddIns, panelName);
        }

        internal static ImageSource ByteArrayToImageSource(byte[] imageData, int size)
        {
            var bitmap_img = new BitmapImage();
            var memory_stream = new MemoryStream(imageData);
            bitmap_img.BeginInit();
            bitmap_img.StreamSource = memory_stream;
            bitmap_img.EndInit();
            var resized = new TransformedBitmap(
                bitmap_img,
                new ScaleTransform(
                    (double)size / bitmap_img.PixelWidth,
                    (double)size / bitmap_img.PixelHeight));
            return resized;
        }
    }
}
