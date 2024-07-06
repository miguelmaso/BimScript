using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;

namespace BimScript
{
    [Transaction(TransactionMode.Manual)]
    internal class ConfigurationCmd : IExternalCommand
    {
        public Result Execute(ExternalCommandData commandData, ref string message, ElementSet element)
        {
            var form = new ConfigurationWpf();
            form.ShowDialog();
            return Result.Succeeded;
        }
    }
}
