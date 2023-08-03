from django.contrib import admin, messages
from django.db.models import QuerySet
from .models import Movie


class RatingFilter(admin.SimpleListFilter):
    title = "Фильтр по рейтингу"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("<40", "Низкий рейтинг"),
            ("<55", "Средний рейтинг"),
            (">80", "Высокий рейтинг"),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "<40":
            return queryset.filter(rating__lt=40)
        if self.value() == "<55":
            return queryset.filter(rating__lt=75)
        if self.value() == ">80":
            return queryset.filter(rating__gt=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "rating", "currency", "year", "budget", "rating_status"]
    list_editable = ["rating", "budget", "currency", "year"]
    list_per_page = 5
    actions = ["set_dollars", "set_euro"]
    search_fields = ["name__startswith", "rating"]
    list_filter = ["name", "currency", RatingFilter]
    prepopulated_fields = {"slug": ("name",)}

    @admin.display(ordering="rating")
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return "Фильм не очень"
        if mov.rating < 70:
            return "Норм"
        if mov.rating <= 86:
            return "Ваще кайф"
        else:
            return "Шедевр"

    @admin.action(description="Установить валюту в долларах")
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description="Установить валюту в евро")
    def set_euro(self, request, queryset: QuerySet):
        count_updated = queryset.update(currency=Movie.EUR)
        self.message_user(
            request, f"Было обновлено {count_updated} запмсей", messages.ERROR
        )
