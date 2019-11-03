import {Injectable} from '@angular/core';
import {HttpHeaders, HttpClient, HttpErrorResponse} from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';
import {City} from './city.model';

@Injectable()
export class WeatherApiService {

    constructor(private http: HttpClient) {
    }


    getCities(): Observable<City[]> {
        return this.http.get<City[]>('http://127.0.0.1:5000/cities');

    }

}
