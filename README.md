
# مختصر گزارش آزمایش


# پاسخ سوالات آخر آزمایش 

## 1. پوشه‌ی .git چیست؟ چه اطلاعاتی در آن ذخیره می‌شود؟ با چه دستوری ساخته می‌شود؟
یک پوشه است که با دستور git init ساخته می شود و حاوی تمام اطلاعات لازم برای پروژه و کلیه اطلاعات مربوط به commit ها، آدرس مخزن remote و غیره است. همچنین شامل یک گزارش است که تاریخچه commit را ذخیره می کند. این گزارش می تواند به شما کمک کند تا به نسخه مورد نظر کد بازگردید.

## 2.منظور از atomic بودن در atomic commit و atomic pull-request چیست؟
منظور این است که هر commit یا pull request در کوچکترین سایز ممکن باشد به صورتی که یک کار معنادار کوچک انجام دهند که به راحتی قابل فهم، بازگشت و یا تغییر باشد. برای جلوگیری از بوجود آمدن پیچیدگی در کامیت ها و تغییرات مناسب است.

## 3.تفاوت دستورهای fetch و pull و merge و rebase را بیان کنید.
* دستور Git Fetchبه مخزن محلی می‌گوید که تغییراتی در مخزن راه دور اتفاق افتاده اند به چه صورت است، بدون وارد کردن تغییرات در مخزن محلی.
* از طرف دیگر Git Pull کپی تغییرات دایرکتوری راه دور را به مخزن محلی می آورد.
**به عبارتی: Git pull = git fetch + git merge
هم git merge  و هم git rebase دو شاخه را با هم ادغام می کنند اما به روش های مختلف:
* در git merge سابقه هردو شاخه قبلی دست نخورده باقی می ماند و در یک state جدید دو شاخه با یکدیگر ادغام می گرند. 
* این در حالی است که در git rebase ما یکی از شاخه ها را به انتهای شاخه دیگر جابجا کرده و عملا یک شاخه در نتیجه خواهیم داشت و اینگونه دو شاخه مورد نظر ادغام می شوند.

## 4.تفاوت چهار دستور reset و revert و restore را بیان کنید.
- دستور reset مربوط به به روز رسانی شاخه شما، حرکت  بر روی شاخه به منظور افزودن یا حذف commit ها از شاخه است. این عملیات تاریخچه commit را تغییر می دهد.
- دستور revert با ایجاد یک commit جدید، تغییرات ایجاد شده توسط سایر commit ها را برگردانده می شود.
- در restore شاخه بروز رسانی نمی شود بلکه تغییراتی که در stage area یا working tree انجام شده است بازنشانی می شود به صورتی که فایل ها یا تغییر های انجام شده به حالت unstaged یا discard در آورده می شوند.

## 5.منظور از stage چیست؟ دستور stash چه کاری را انجام می‌دهد؟
- منظور از Stage حالتی است که تغییراتی که بر روی پروژه یا شاخه انجام شده اند هنوز commit نشده اند ولی ذخیره شده اند که به محیط ذخیره شده هم stage area گفته می شود، ما می توانیم این تغییرات را با restore به حالت unstage در آوریم یا اینکه آن ها را کامیت کنیم.
- در stash تمام تغییرات انجام شده که هنوز کامیت نشده اند شامل staged & unstaged در جایی ذخیره می شوند برای استفاده بعدی و از working copy به صورت موقت برداشته می شوند و در صورت لزوم بعدا بازنشانی می گردند.

## 6.مفهوم snapshot به چه معناست؟
گیت یک سیستم مدیریت نسخه است که مسیر تغییرات و انجام عملیات های پروژه را ذخیره می کند و گیت این کار را با استفاده از ذخیره snapshot هایی از پروژه در مراحل مختلف و بعد از هر کامیت انجام می دهد.