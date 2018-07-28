from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import *
from .forms import *
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

# Create your views here.
def index(request):
	if request.method == 'POST':
		register_user_name = request.POST.get('register_user_name')
		register_pass_word = request.POST.get('register_pass_word')
		register_pass_word_again = request.POST.get('register_pass_word_again')

		user_name = request.POST.get('user_name')
		pass_word = request.POST.get('pass_word')
		if register_user_name != None and register_pass_word and register_pass_word_again != None:
			new_user = User(user_name = register_user_name, pass_word = register_pass_word)
			users = User.objects.filter(user_name__exact=new_user.user_name)
			if users:
				return HttpResponse('用户名已经存在')
			elif register_pass_word_again != register_pass_word:
				return HttpResponse('两次密码不一致')
			else:
				new_user.save()
				return HttpResponseRedirect(reverse('user', args = [new_user.user_id]))
		if user_name != None and pass_word != None:
			old_user = User.objects.filter(user_name__exact=user_name, pass_word__exact=pass_word)
			if old_user:
				return HttpResponseRedirect(reverse('user', args = [old_user[0].user_id]))
			else:
				return HttpResponse('用户名或密码错误,请重新登录')
	return render(request, 'index.html')

def user(request, user_id):
	user = User.objects.get(user_id = user_id)
	context = {'user': user}
	return render(request, 'user.html', context)

# def new_user(request):
# 	flag = True
# 	if request.method != 'POST':
# 		form = UserForm()
# 	else:
# 		form = UserForm(request.POST)
# 		if form.is_valid() and form.cleaned_data['user_name'] and form.cleaned_data['pass_word']:
# 			new_user = form.save(commit = False)
# 			users = User.objects.filter(user_name__exact=new_user.user_name)
# 			if new_user.user_name not in [i.user_name for i in users]:
# 				new_user.save()	
# 				return HttpResponseRedirect(reverse('user', args = [new_user.user_id]))
# 			else:
# 				flag = False
# 				form = UserForm()
# 	context = {'form': form, 'flag': flag}
# 	return render(request, 'new_user.html', context)

# def old_user(request):
# 	flag = True
# 	if request.method != 'POST':
# 		form = UserForm()
# 	else:
# 		form = UserForm(request.POST)
# 		if form.is_valid():
# 			user_name = form.cleaned_data['user_name']
# 			pass_word = form.cleaned_data['pass_word']
# 			old_user = User.objects.filter(user_name__exact=user_name, pass_word__exact=pass_word)
# 			if old_user:
# 				return HttpResponseRedirect(reverse('user', args = [old_user[0].user_id]))
# 			else:
# 				flag = False
# 				#return HttpResponse('用户名或密码错误,请重新登录')
# 	context = {'form': form, 'flag': flag}
# 	return render(request, 'old_user.html', context)

def reader(request, user_id):
	flag = False
	user = User.objects.get(user_id = user_id)
	readers = Reader.objects.filter(user = user)
	if readers:
		flag = True
	if request.method != 'POST':
		form = ReaderForm()
	else:
		form = ReaderForm(request.POST)
		if form.is_valid():
			reader = form.save(commit = False)
			reader.user = user
			reader.save()
			return HttpResponseRedirect(reverse('user', args = [user.user_id]))
	context = {'form': form, 'user': user, 'flag': flag, 'readers': readers}
	return render(request, 'reader.html', context)

def search(request, user_id):
	user = User.objects.get(user_id = user_id)
	class_infos = ClassInfo.objects.all()                 #also dict!
	authors = BookInfo.objects.values('author').distinct()#also dict!
	book_names = BookInfo.objects.values('book_name').distinct()
	publishers = BookInfo.objects.values('publisher').distinct()
	pub_dates = BookInfo.objects.values('pub_date').distinct()

	book_name = request.POST.get('book_name')
	author = request.POST.get('author')
	publisher = request.POST.get('publisher')
	pub_date_raw = request.POST.get('pub_date')
	class_info_id = request.POST.get('class_info_id')
	d = {'Jan': 1,
		 'Feb': 2,
		 'March': 3,
		 'April': 4,
		 'May': 5,
		 'June': 6,
		 'July': 7,
		 'Aug': 8,
		 'Sept': 9,
		 'Oct': 10,
		 'Nov': 11,
		 'Dec': 12
		}
	books = BookInfo.objects.all()
	query_condition = ''
	pub_date = ''
	if pub_date_raw != None and pub_date_raw != 'all':
		pub_date_raw = pub_date_raw.replace(',', '')
		pub_date_raw = pub_date_raw.replace('.', '')

		pub_date_list = pub_date_raw.split(' ')
		pub_date = pub_date_list[2] + '-' + '{:0>2d}'.format(d[pub_date_list[0]]) + '-' + pub_date_list[1].rjust(2, '0')
		books = BookInfo.objects.filter(pub_date = pub_date)
		query_condition += pub_date
	if class_info_id != None and str(class_info_id) != 'all': #ROM foreigned not only id but also object!
		books = books.filter(class_info = ClassInfo.objects.get(class_info_id = class_info_id))
		query_condition += '  ' + str(ClassInfo.objects.get(class_info_id = class_info_id).class_intro)
	if publisher != None and publisher != 'all':
		books = books.filter(publisher = publisher)
		query_condition += '  ' + str(publisher)
	if book_name != None and book_name != 'all':
		books = books.filter(book_name = book_name)
		query_condition += '  ' + str(book_name)
	context = {	'user': user, 
				'class_infos': sorted(class_infos, key = lambda x: x.class_intro), #object
				'authors': sorted(authors, key = lambda x: x['author']),           #divt{}
				'book_names': sorted(book_names, key = lambda x: x['book_name']),  #dict{}
				'publishers': sorted(publishers, key = lambda x: x['publisher']),  #dict{}
				'pub_dates': sorted(pub_dates, key = lambda x: x['pub_date']),     #dict{}
				'books': books,
				'query_condition': query_condition
			  }

	return render(request, 'search.html', context)

def card_register(request, user_id):
	user = User.objects.get(user_id = user_id)
	readers = Reader.objects.filter(user = user)
	readers_cards = { }

	for areader in readers:
		cards = Card.objects.filter(reader = areader)
		readers_cards[areader.reader_id] = [i.card_id for i in cards]
	#readers:     [reader object]
	#reader_cards:{reader_id, [my cards' card_id]}

	context = {'user': user, 'readers': readers, 'readers_cards': readers_cards}
	return render(request, 'card_register.html', context)

def registering(request, user_id, reader_id):
	user = User.objects.get(user_id = user_id)
	try:
		reader = Reader.objects.get(reader_id = reader_id)
	except:
		return HttpResponse('这不是reader!')
	cards = Card.objects.filter(reader = reader)
	readers = Reader.objects.filter(user = user)
	if reader not in readers:
		return HttpResponse('这不是你的reader!')
	if request.method == 'POST': 
		# 办理借书证
		times = request.POST.get('times')
		if times != None:
			times = int(times) // 10
			new_card = Card(remain_times = times, reader = reader)
			if len(cards) < 8:
				new_card.save()
		cards = Card.objects.filter(reader = reader)
		for c in cards:
			# 借书证充值
			recharge = request.POST.get(str(c.card_id))
			if recharge != None:
				if int(recharge) >= 0:
					c.remain_times += int(recharge)
					c.save()
				else:
					c.delete()
		cards = Card.objects.filter(reader = reader)	
	context = {'user': user, 'reader': reader, 'cards': cards}
	return render(request, 'registering.html', context)

def choose(request, user_id, book_id):
	user = User.objects.get(user_id = user_id)
	readers = Reader.objects.filter(user = user)
	book = BookInfo.objects.get(book_id = book_id)
	readers_cards = { }
	book_cards = [i.card for i in Borrow.objects.all() if i.book == book and not i.return_back]
	for areader in readers:
		cards = Card.objects.filter(reader = areader)
		readers_cards[areader.reader_id] = cards
	#readers:     [reader object]
	#reader_cards:{reader_id, [my cards' card_id]}
	if request.method == 'POST':
		for r in readers:
			# 选定读者
			card_id = request.POST.get(str(r.reader_id))
			if card_id != None:
				card = Card.objects.get(card_id = int(card_id))
				if card.remain_times <= 0:
					return  HttpResponse('别闹了, 你的借书次数已经用完')
				else:
					return HttpResponseRedirect(reverse('borrow', args = [user_id, book_id, int(card_id)]))
	context = {'user': user, 'book': book, 'readers': readers, 
			   'readers_cards': readers_cards, 'book_cards': book_cards}
	return render(request, 'choose.html', context)


def borrow(request, user_id, book_id, card_id):
	user = User.objects.get(user_id = user_id)
	try:
		book = BookInfo.objects.get(book_id = book_id)
	except:
		return HttpResponse('这不是book!')
	try:
		card = Card.objects.get(card_id = card_id)
	except:
		return HttpResponse('这不是card!')
	reader = card.reader
	new_borrow = Borrow(card = card, book = book)

	if request.method == 'POST':
		ensure = request.POST.get('ensure')
		change_card = request.POST.get('change_card')
		change_book = request.POST.get('change_book')
		if ensure == '1':
			new_borrow.save()
			book.remain -= 1
			book.save()
			card.remain_times -= 1
			card.save()
			return HttpResponseRedirect(reverse('search', args = [user_id]))
		if change_card == '1':
			return HttpResponseRedirect(reverse('choose', args = [user_id, book_id]))
		elif change_book == '1':
			return HttpResponseRedirect(reverse('search', args = [user_id]))
	context = {'user': user, 'reader': reader, 'book': book, 'card': card, 'new_borrow': new_borrow }
	return render(request, 'borrow.html', context)


def borrow_history(request, user_id):
	user = User.objects.get(user_id = user_id)
	borrows = filter(lambda x: x.card.reader.user == user, Borrow.objects.all())
	context = {'user': user, 'borrows': sorted(borrows, key = lambda x: x.when)}
	if request.method == 'POST':
		borrow_id = request.POST.get('return_back')
		if borrow_id != None:
			try:
				borrow = Borrow.objects.get(borrow_id = borrow_id)
			except:
				return HttpResponse('Sorry, you can\'t return it')
			if borrow.return_back:
				return render(request, 'borrow_history.html', context)
			else:
				card = borrow.card
				book = borrow.book
				card.remain_times += 1
				card.save()
				book.remain += 1
				book.save()
				borrow.return_back = 1
				borrow.save()
	borrows = filter(lambda x: x.card.reader.user == user, Borrow.objects.all())
	context = {'user': user, 'borrows': sorted(borrows, key = lambda x: x.when)}
	return render(request, 'borrow_history.html', context)
