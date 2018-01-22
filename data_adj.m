clear all;
clc;

cd(matlabroot)
cd('C:\Users\Nishant\Documents\MATLAB\New folder');
ds = dataset('XLSFile','dataset_2.xlsx');

m=zeros(548,548);
m1=zeros(548,548);
n= zeros(548,548);

for i=1:548
    for j=1:548
        if((ds{i,2}-ds{j,2})<0.5)&&((ds{i,2}-ds{j,2})>-0.5)
            n(i,j) = 1;
            m1 = m1 + n;
            n = zeros(548,548);
        end
    end
end


for i=1:548
    for j=1:548
        for k=3:13
            if isequal(ds{i,k} ,ds{j,k})
                n(i,j) = 1;
                m = m + n;
                n = zeros(548,548);
            end
        end
    end
end

X=m1+m
