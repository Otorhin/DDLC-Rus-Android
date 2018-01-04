image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        pause 7
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11
    y "Привет, [player]!"
    y "Я ждала тебя."
    y "Ты готов продолжить читать?"
    y "Я принесла свой лучший чай--"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "Моника!"
    n "Я сказала тебе не--"
    n "Угх..."
    n "Она опять опаздывает?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "Ты, как обычно, невнимательна, Нацуки."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n "Что-что?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "Ты каждый раз будешь перебивать меня своими неугомонными криками?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n "О чём ты говоришь?!"
    n "Ты говоришь это так, будто я регулярно это делаю."
    n "Я просто не заметила, ясно? Прошу прощения."
    n "Вот серьёзно... что на тебя нашло?"
    if n_appeal >= 2:
        n "Смотри..."
        n "Я вчера немного подумала о случившемся."
        n "Я была чересчур агрессивна в тот раз..."
        n "Мне показалось, что на меня давят."
        n "Но я знаю, что мы совместно занимаемся подготовкой."
        n "Ещё один член нам не повредит, если он клёвый..."
        n "И, я думаю, ещё одна девочка будет неплохим пополнением..."
        n "Так что..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y "Нацуки..."
        $ style.say_dialogue = style.edited
        y "Всем пофиг."
        y "Почему бы тебе не пойти и не заняться поиском монеток под торговыми автоматами или ещё чем-нибудь?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "--!"
        n "..."
        n "..."
        show natsuki at thide
        hide natsuki
        pause 1.0
        show monika 1g at l31
        m "Ах, блин..."
        m "Опять я осталась одна!"
        show yuri zorder 3 at f32
        y "Ты опять практиковалась играть на пианино?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m "Да..."
        m "Ахаха..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y "Ты, должно быть, очень решительна."
        y "Организовывать этот клуб и всё ещё находить время для пианино..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m "Ну, может быть, не решительна..."
        m "А, мне кажется, страстна."
        m "Страсть и мотивирует меня стараться с подготовкой к фестивалю."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y "Я?"
        y "Н-ничего..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y "Это настолько плохо...?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "Видишь, {i}это{/i} так."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y "Я разберусь!"
        y "Это даже не заслуживает внимания..."
        y "Просто в последнее время я чувствую себя на грани..."
        y "Н-нам не нужно об этом говорить!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "Ну, я просто подумала, что стоит поднять эту тему."
        n "Не то чтобы я волновалась..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "Ах, блин..."
        m "Опять я осталась одна!"
        show natsuki zorder 3 at f33
        n "Ну, [player] только что пришёл."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y "Ты опять практиковалась играть на пианино?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m "Да..."
        m "Ахаха..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y "Ты должно быть очень решительна."
        y "Организовывать этот клуб и всё ещё находить время для пианино..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m "Ну, может быть, не решительна..."
        m "А, мне кажется, страстна."
        m "Страсть и мотивирует меня стараться с подготовкой к фестивалю..."
        m "Эм..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m "Да..."
        m "Я-я забыла..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y "Эм, про случившееся, Нацуки..."
        y "Мы все вчера разговаривали и..."
        y "Ну... Мы решили, что тоже хотим помочь с подготовкой к фестивалю."
        y "И всё же...!"
        y "Я понимаю, что ты чувствуешь, говоря о том, что не хочешь, чтобы клуб изменился."
        y "Я думаю, что мы все считаем так же."
        y "Так что, если мы будем работать вместе, этот клуб не претерпит нежелательных изменений."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y "Эм, и ещё..."
        y "Если ты поможешь нам с фестивалем..."
        y "...То я куплю тебе мангу!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        n "Ахахаха!"
        n "Прости, последние слова были очень смешными."
        n "Смотри..."
        n "Я вчера немного подумала о случившемся."
        n "Я была более агрессивна чем обычно в тот раз..."
        n "Мне показалось, что на меня давят."
        n "Но я знаю, что мы совместно занимаемся подготовкой."
        n "Ещё один член нам не повредит, если он клёвый..."
        n "И, я думаю, ещё одна девочка будет неплохим пополнением..."
        n "...Но важнее то, что мне будет не очень приятно смотреть на то, как вы облажаетесь на фестивале из-за того, что я отказалась помочь!"
        n "Я же профи, помните!"
        n "Так что я тоже помогу, чтобы всё прошло гладко."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y "Спасибо, Господи..."
        y "Разве это не замечательно, Моника?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "...Моника?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "Ах--"
        m "Да, это замечательно!"
        m "Без тебя всё было бы по другому, Нацуки."
    m "В любом случае, [player]..."
    m "Чем ты хочешь сегодня заняться?"
    m "Я думала, что мы могли бы--"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y "У нас уже есть на сегодня планы."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m "Ах..."
    m "Это правда, Юри?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y "Да, это так."
    y "[player] уже занят книгой, которую мы вместе читаем."
    y "Разве ты не рада, что я привлекла его к литературе, Моника?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m "Я..."
    m "Наверное..."
    m "Я просто--"
    m "На самом деле это не имеет значения."
    m "Вообще никакого."
    m "Вы, ребята, можете делать что хотите."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y "{i}(Да!){/i}{w=0.5}{nw}"
    y "Эмм... спасибо за понимание, Моника."
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22 from _call_yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2]) from _call_expression_1
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "Так, всем внимание!"
    m "Наступило время разобраться с подготовкой к фестивалю."
    m "Давайте поскорее разберёмся с этим."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "Господи..."
        n "Почему сегодня такое странное настроение?"
        n "Посмотри, даже Юри обратила на это внимание."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Уу..."
    y "Тяжёлый воздух -- это частый признак того, что может произойти что-то плохое..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "Может, мы просто приступим к делу?"
    m "Я распечатаю и подготовлю все брошюры с поэмами."
    if n_appeal >= 2:
        m "Нацуки, ты можешь сделать кексы."
        m "Я знаю, что ты хороша хотя бы в этом."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Нацуки, я подумала--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n "Я хочу сделать кексов!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m "...Да."
        m "Хорошо, что ты меня поняла."
    m "Юри, ты можешь..."
    m "...Да без разницы."
    m "Помогай так, как считаешь нужным."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y "Моника..."
    y "Я не бесполезная!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "Я-я знаю!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y "Я уже знаю, чем бы хотела заняться."
    y "Мы не можем проводить мероприятие без подходящей атмосферы."
    y "Так что я решила заняться декорациями и подготовкой подходящего освещения."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "Вот видишь?"
    m "Это отличная идея!"
    m "Теперь каждому из нас есть чем заняться."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y "Эм?"
    y "А как же [player]?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "[player] будет помогать мне."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n "Подожди, тебе?"
    n "У тебя самая простая работа, Моника!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m "Простите, но с этим уже ничего не поделать."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n "Ещё чего!"
    n "Что ты задумала?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y "Я-я согласна с Нацуки!"
    y "Твоя работа рассчитана на одного человека..."
    y "А я бы не отказалась от пары лишних рук."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n "Я тоже!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y "Что, твои кексы?"
    y "Пощади."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n "С хуя ли {i}ты{/i} так решила?!"
    n "Ты только и думаешь о книгах и о том, как бы сделать так, чтобы [player] остался с тобой наедине."
    n "Ты {i}и{/i} Моника!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m "Эй!"
    m "Я даже ничего не сделала!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n "Хорошо, пусть тогда [player] выберет, чтобы ты не злоупотребляла своим положением."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m "Я не... злоупотребляю."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y "Да, злоупотребляешь, Моника."
    y "Просто пусть выберет [player], ладно?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "Хорошо!"
    m "Ладно."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n "Господи..."
    n "[player], я знаю, как тебе надоели эти двое."
    n "Мы просто можем--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y "Нацуки, заткнись нахуй и дай ему выбрать."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n "{i}Ты{/i} заткнись!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m "Божечки..."
    m "Это никогда не закончится. Просто сделай выбор, хорошо?"
    show monika zorder 2 at t32
    $ madechoice = renpy.display_menu([("Нацуки.", "natsuki"), ("Юри.", "yuri"), ("Моника.", "monika")], screen="rigged_choice")


    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        pause 3.0
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri

    m "Ура, ты выбрал меня!"
    m "Мы можем встретиться у твоего дома на выходных."
    m "Я обещаю, что будет весело."
    m "В воскресенье будет нормально?"
    show natsuki 1e zorder 3 at f31
    n "Ты, блять, издеваешься?"
    n "Это совершенно не честно!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m "Всё честно, Нацуки."
    m "Это то, что он выбрал."
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "Нет, это не честно!"
    y "С тобой [player], и ты загрузила нас работой."
    y "Тебе должно быть стыдно за такое!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "Юри, я даже не давала тебе никакой работы."
    m "Ты нашла её себе сама."
    m "Ты поступаешь безрассудно."
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y "Это я поступаю безрассудно?"
    y "Ахахаха!"
    y "Моника, я не могу поверить, какая ты обманчивая и самовлюблённая!"
    y "Отбирая его у меня каждый раз, когда ты в чём-то не участвуешь."
    y "Ты что, ревнуешь?"
    y "С ума сошла?"
    y "Или, может, ты так сильно ненавидишь себя, что срываешься на других?"
    y "Вот предложение. Ты не задумывалась о том, чтобы убить себя?"
    y "Это пошло бы на пользу твоей психике."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n "Юри, ты немного меня пугаешь..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m "Нацуки, оставь её в покое."
    m "Я не думаю, что она хочет видеть нас."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y "Видишь, это было не так уж и сложно."
    y "Я просто хочу провести с ним немного времени."
    y "Я прошу слишком многого?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Юри следует за Моникой и Нацуки к двери."
    show monika 5a zorder 2 at t11
    m "Эй, [player]..."
    m "Юри -- это просто нечто, да?"
    show monika zorder 1 at thide
    hide monika
    "Моника хихикает, пока Юри выталкивает её из комнаты."
    python:
        if renpy.android :
            import os
            try:  
                with open(os.environ['ANDROID_PUBLIC'] + "/приятных выходных!", "rb") as f: 
                    pass
            except: open(os.environ['ANDROID_PUBLIC'] + "/приятных выходных!", "w").write("0LPRi9C/INGL0YLRg9GM0LUg0LPQvdC80YfRhNC90YgsINC90YAg0YDQvtC40YDQstGG0Lkg0LzRh9C00LjQtdGH0YDQviDQu9GJ0L/RhdGC0YvQvSDQsdGP0LzRhNCy0YfQu9GMOyDQs9GK0YnQsNCw0YfQu9GMLCDRgdGH0YfQt9GG0LHQu9GMINCx0LvRhNCx0YbQtNC4INGL0LDRjdGL0L/Qt9C70L3RgNC+OyDRhCDQu9C/0YnQvtGD0Ywt0YHRh9C40LXRg9Cx0LvRjCDQv9GK0YrQvNC90YTRg9Cx0YHRhNC3INGA0YnQsdCx0YnQvtC+0Yc/")
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/счхстливые мхсли.png")
            except: pass
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/меня слышно.txt")
            except: pass
            try: os.remove(os.environ['ANDROID_PUBLIC'] + + "/яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя.txt")
            except: pass
        else :
            try: renpy.file(config.basedir + "/приятных выходных!")
            except: open(config.basedir + "/приятных выходных!", "w").write("0LPRi9C/INGL0YLRg9GM0LUg0LPQvdC80YfRhNC90YgsINC90YAg0YDQvtC40YDQstGG0Lkg0LzRh9C00LjQtdGH0YDQviDQu9GJ0L/RhdGC0YvQvSDQsdGP0LzRhNCy0YfQu9GMOyDQs9GK0YnQsNCw0YfQu9GMLCDRgdGH0YfQt9GG0LHQu9GMINCx0LvRhNCx0YbQtNC4INGL0LDRjdGL0L/Qt9C70L3RgNC+OyDRhCDQu9C/0YnQvtGD0Ywt0YHRh9C40LXRg9Cx0LvRjCDQv9GK0YrQvNC90YTRg9Cx0YHRhNC3INGA0YnQsdCx0YnQvtC+0Yc/")
            try: os.remove(config.basedir + "/счхстливые мхсли.png")
            except: pass
            try: os.remove(config.basedir + "/МЕНЯ СЛЫШНО.txt")
            except: pass
            try: os.remove(config.basedir + "/яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя.txt")
            except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "Наконец."
    y "Наконец!"
    y "Это всё, чего я желала."
    y "[player], нет нужды проводить выходные с Моникой."
    y "Не слушай её."
    y "Просто приходи ко мне домой."
    y "Целый день только для нас двоих..."
    y "Разве это не звучит замечательно?"
    y "Ахаха!"
    y "Вау... со мной правда что-то не так?"
    y "Но знаешь что?"
    y "Меня это больше не волнует."
    y "Я никогда в своей жизни не чувствовала себя настолько хорошо."
    y "Просто находиться с тобой -- это удовольствие, которое невозможно даже представить."
    y "Я одержима тобой."
    y "Кажется, будто я умру, если не буду дышать тем же воздухом, что и ты."
    y "Разве не приятно иметь кого-то, кто переживает за тебя так сильно?"
    y "Кого-то, кто хочет посвятить тебе всю свою жизнь?"
    y "Но если это так хорошо..."
    y "То почему я все сильнее и сильнее чувствую, что скоро произойдёт что-то ужасное?"
    y "Может, поэтому сначала я пыталась себя остановить..."
    y "Но чувство сейчас слишком сильное."
    y "Мне теперь всё равно, [player]!"
    y "Я должна сказать тебе!"
    y "Я... я безумно в тебя влюблена!"
    y "Кажется, будто каждый сантиметр моего тела... каждая капля крови... кричит твоё имя."
    y "Меня больше не волнуют последствия!"
    y "Меня не волнует, подслушивает ли Моника!"
    y "Пожалуйста, [player], просто знай, насколько сильно я тебя люблю."
    y "Я люблю тебя настолько сильно, что даже ублажала себя ручкой, которую украла у тебя."
    y "Я просто хочу снять с тебя кожу и слиться с тобой."
    y "Я хочу себе всего тебя."
    y "И я буду только твоей."
    y "Разве это не звучит прекрасно?"
    y "Скажи мне, [player]."
    y "Скажи, что хочешь быть моим возлюбленным."
    y "Ты принимаешь моё признание?"

    menu:
        "Да.":
            jump yuri_kill
        "Нет.":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    pause 1.0


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11
    y "...Ахахаха."
    y "Ахахахахахахаха!"
    $ style.say_dialogue = style.normal
    y "Ахахахахахахахахаха!"
    $ style.say_dialogue = style.edited
    y "АХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХ{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 2.0

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    python:
        _history_list = []
        m.add_history(None, "", """Добро пожаловать в Литературный Клуб! Моей мечтой всегда была идея: создать нечто особенное из того, что я люблю. Сейчас, как член клуба, ты можешь помочь сбыться моей мечте в этой милой игре! Каждый день полон разговоров и весёлых занятий с моими обожаемыми и уникальными членами клуба: Сайори, юный луч света, что более всего ценит счастье; Нацуки, обманчиво милая девушка, которая может больно ужалить; Юри, робкая и загадочная, что находит покой в мире книг;... И, конечно, Моника -- глава клуба! Это -- я!Я очень рада, что ты со всеми подружишься, и поможешь сделать Литературный Клуб более привлекательным для его членов. И я уже могу сказать, что ты очень милый! Ты ведь пообещаешь уделить мне больше всего внимания? Добро пожаловать в Литературный Клуб! Моей мечтой всегда была идея: создать нечто особенное из того, что я люблю. Сейчас, как член клуба, ты можешь помочь сбыться моей мечте в этой милой игре! Каждый день полон разговоров и весёлых занятий с моими обожаемыми и уникальными членами клуба:Сайори, юный луч света, что более всего ценит счастье;Нацуки, обманчиво милая девушка, что может больно ужалить;Юри, робкая и загадочная, что находит покой в мире книг;... И, конечно, Моника -- глава клуба! Это -- я!Я очень рада, что ты со всеми подружишься, и поможешь сделать Литературный Клуб более любимым для его членов. И я уже могу сказать, что ты очень милый! Ты ведь пообещаешь уделить мне больше всего внимания? Добро пожаловать в Литературный Клуб! Моей мечтой всегда была идея: создать нечто особенное из того, что я люблю. Сейчас, как член клуба, ты можешь помочь сбыться моей мечте в этой милой игре!Каждый день полон разговоров и веселых занятий с моими обожаемыми и уникальными членами клуба:Сайори, юный луч света, что более всего ценит счастье;Нацуки, обманчиво милая девушка, что может больно ужалить;Юри, робкая и загадочная, что находит покой в мире книг;...И, конечно, Моника -- глава клуба! Это -- я!Я очень рада, что ты со всеми подружишься, и поможешь сделать Литературный Клуб более любимым для его членов. И я уже могу сказать, что ты очень милый! Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?""")

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:

    python:
        if renpy.android :
            import os
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/приятных выходных!")
            except: pass
        else :
            try: os.remove(config.basedir + "/приятных выходных!")
            except: pass

    $ persistent.autoload = "yuri_kill_3"
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Отлично, настало время фестиваля!"
    show natsuki 4k zorder 2 at t11
    n "Ого, ты пришёл раньше меня?"
    n "Я думала, что пришла рань--{nw}"
    show natsuki scream at h11
    n "Э!"
    n "АААААААААААААААААА!!!"
    pause 1.0
    show natsuki scream at h11
    pause 0.75
    show natsuki vomit at h11
    pause 1.25
    show natsuki at lhide
    hide natsuki
    "Нацуки убегает."
    m "..."
    show monika 2b zorder 2 at t11
    m "Я здесь!"
    m "[player], что-то случилось?"
    m "Нацуки только что пробежала мимо..."
    m "... Ох..."
    m "...Ох."
    m "..."
    m "Ахахаха!"
    m "Вот ведь."
    m "Стоп, ты был здесь все выходные, [player]?"
    m "О божечки..."
    m "Я не думала, что скрипт игры сломан настолько сильно."
    m "Прошу прощения!"
    m "Наверное, было очень скучно..."
    m "Сейчас я всё поправлю, хорошо?"
    m "Просто дай мне секунду..."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr успешно удалён.") from _call_updateconsole_15
    $ delete_character("yuri")
    pause 1.0
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr успешно удалён.") from _call_updateconsole_16
    $ delete_character("natsuki")
    pause 1.0
    m "Я почти закончила."
    m "Я просто хочу кекс!"
    $ gtext = glitchtext(10)
    "Моника поднимает фольгу с подноса [gtext] и берёт кексик."
    m "Серьёзно, они лучшие!"
    m "Я хотела съесть один, раз уж это моя последняя возможность."
    m "Знаешь, перед тем как они перестанут существовать."
    m "...И всё же, я не должна заставлять тебя больше ждать."
    m "Просто потерпи ещё немножко, ладно?"
    m "Это займёт всего секунду."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.full_restart(transition=None, label="splashscreen")

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
