select Security as Company, GICS_Sector as Sector, GICS_Sub_Industry as Industry, CIK as Assests 
from securities
where CIK > 1000;