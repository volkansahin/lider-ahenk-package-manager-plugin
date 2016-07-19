package tr.org.liderahenk.packagemanager.handlers;


import java.util.Set;

import org.eclipse.swt.widgets.Display;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import tr.org.liderahenk.liderconsole.core.handlers.MultipleSelectionHandler;
import tr.org.liderahenk.packagemanager.dialogs.CheckPackageTaskDialog;

public class CheckPackageTaskHandler extends MultipleSelectionHandler {
	private Logger logger = LoggerFactory.getLogger(PackageSourcesTaskHandler.class);

	@Override
	public void executeWithDNSet(Set<String> dnSet) {
		CheckPackageTaskDialog dialog = new CheckPackageTaskDialog(Display.getDefault().getActiveShell(), dnSet);
		dialog.create();
		dialog.open();
	}

}