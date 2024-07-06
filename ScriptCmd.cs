using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;

namespace BimScript
{
    [Transaction(TransactionMode.Manual)]
    internal class ScriptCmd : IExternalCommand
    {
        public Result Execute(ExternalCommandData commandData, ref string message, ElementSet element)
        {
            return Result.Succeeded;
        }
    }
}
